import io
from urllib.parse import urlencode

import pytest

import route
from app.controllers.application import Application
from app.models.classes.portal import PortalAlfabeta


def chamar_wsgi(app, method: str, path: str, query: str = "", form: dict | None = None):
    """Executa uma requisição HTTP diretamente na aplicação WSGI Bottle."""
    body_bytes = b""
    content_type = ""
    if form is not None:
        body_bytes = urlencode(form).encode("utf-8")
        content_type = "application/x-www-form-urlencoded; charset=utf-8"

    environ = {
        "REQUEST_METHOD": method,
        "SCRIPT_NAME": "",
        "PATH_INFO": path,
        "QUERY_STRING": query,
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "8080",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "http",
        "wsgi.input": io.BytesIO(body_bytes),
        "wsgi.errors": io.StringIO(),
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
        "CONTENT_LENGTH": str(len(body_bytes)),
        "CONTENT_TYPE": content_type,
    }

    captured = {}

    def start_response(status, headers, exc_info=None):
        captured["status"] = status
        captured["headers"] = dict(headers)

    chunks = list(app(environ, start_response))
    captured["body"] = b"".join(chunks).decode("utf-8", errors="replace")
    return captured["status"], captured["headers"], captured["body"]


@pytest.fixture
def bmvc_isolado(tmp_path, monkeypatch):
    caminho_prof = tmp_path / "professores.json"
    caminho_aulas = tmp_path / "aulas.json"
    portal_model = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    ctl = Application(portal_model=portal_model)
    monkeypatch.setattr(route, "ctl", ctl)
    return route.app, ctl, caminho_prof, caminho_aulas


def test_bmvc_rotas_publicas_e_static(bmvc_isolado):
    app, _, _, _ = bmvc_isolado

    for path in ["/", "/portal"]:
        status, _, body = chamar_wsgi(app, "GET", path)
        assert status.startswith("200")
        assert "Portal do educador" in body
        assert 'href="/cadastro"' in body

    status, _, body = chamar_wsgi(app, "GET", "/helper")
    assert status.startswith("200")
    assert "BMVC" in body

    status, _, body = chamar_wsgi(app, "GET", "/static/css/portal.css")
    assert status.startswith("200")
    assert "dashboard-container" in body


def test_bmvc_cadastro_e_login_utf8(bmvc_isolado):
    app, ctl, caminho_prof, _ = bmvc_isolado

    status, _, body = chamar_wsgi(app, "GET", "/cadastro")
    assert status.startswith("200")
    assert 'action="/cadastro"' in body

    # Cadastro com acentuação UTF-8
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/cadastro",
        form={
            "nome": "João da Conceição",
            "email": "joao@alfabeta.com",
            "login": "joao",
            "senha": "123",
        },
    )
    assert status.startswith("200")
    assert "Conta criada com sucesso" in body

    # Login duplicado retorna erro na tela de cadastro
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/cadastro",
        form={
            "nome": "Outro João",
            "email": "outro@alfabeta.com",
            "login": "joao",
            "senha": "456",
        },
    )
    assert status.startswith("200")
    assert "já está em uso" in body

    # Login inválido
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/portal",
        form={"login": "joao", "senha": "errada"},
    )
    assert status.startswith("200")
    assert "Login ou senha incorretos" in body
    assert ctl.current_user is None

    # Login válido preserva UTF-8
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/portal",
        form={"login": "joao", "senha": "123"},
    )
    assert status.startswith("200")
    assert "João da Conceição" in body
    assert "JoÃ£o" not in body
    assert ctl.current_user is not None

    # Verifica persistência no JSON
    portal_rec = PortalAlfabeta(str(caminho_prof), str(caminho_prof.parent / "aulas.json"))
    assert portal_rec.autenticar("joao", "123").nome == "João da Conceição"


def test_bmvc_crud_aulas_salario_fim_mes_e_sair(bmvc_isolado):
    app, ctl, caminho_prof, caminho_aulas = bmvc_isolado

    ctl.portal_model.registrar_professor("Maria José", "maria@email.com", "maria", "abc")
    chamar_wsgi(app, "POST", "/portal", form={"login": "maria", "senha": "abc"})

    # Adicionar aula com nome acentuado e data HTML YYYY-MM-DD
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/portal/adicionar",
        form={
            "nome_aluno": "João Pedro",
            "opcao_tipo": "2",  # Fundamental Individual: 16.54
            "data_aula": "2026-11-20",
        },
    )
    assert status.startswith("200")
    assert "João Pedro" in body
    assert "JoÃ£o" not in body
    assert "20/11/26" in body

    # Alterar aula para Fim de Semana (37.50)
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/portal/alterar",
        form={
            "indice": "0",
            "novo_nome": "João Pedro Júnior",
            "nova_data": "2026-11-22",
            "nova_opcao": "5",
        },
    )
    assert status.startswith("200")
    assert "Aula atualizada com sucesso" in body
    assert "João Pedro Júnior" in body
    assert "22/11/26" in body
    assert "37,50" in body

    # Histórico de aulas
    status, _, body = chamar_wsgi(app, "GET", "/portal", query="aba=historico")
    assert status.startswith("200")
    assert "Histórico de Aulas" in body
    assert "João Pedro Júnior" in body

    # Salário com vale-transporte (1 dia * 11.00 = 11.00 + 37.50 = 48.50)
    status, _, body = chamar_wsgi(app, "GET", "/portal/salario")
    assert status.startswith("200")
    assert "48,50" in body

    # Salário sem vale-transporte (37.50)
    status, _, body = chamar_wsgi(
        app,
        "POST",
        "/portal/salario",
        form={"tem_vt": "nao"},
    )
    assert status.startswith("200")
    assert "37,50" in body
    assert "Não optante" in body

    # Fim do mês persiste no JSON
    status, _, body = chamar_wsgi(app, "POST", "/portal/fim-do-mes")
    assert status.startswith("200")
    assert "1 aulas foram arquivadas" in body

    portal_recarregado = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    prof_rec = portal_recarregado.autenticar("maria", "abc")
    assert prof_rec.agenda.esta_vazia()

    # Sair redireciona e limpa usuário logado
    status, headers, _ = chamar_wsgi(app, "GET", "/sair")
    assert status.startswith(("302", "303"))
    assert headers["Location"].endswith("/portal")
    assert ctl.current_user is None
