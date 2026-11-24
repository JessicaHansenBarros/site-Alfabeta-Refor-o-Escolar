import json

import pytest

from app.models.classes.agenda import AgendaMensal
from app.models.classes.aluno import Aluno
from app.models.classes.aula import (
    Aula,
    AulaFimDeSemana,
    AulaFundamentalColetivo,
    AulaFundamentalIndividual,
    AulaMedioColetivo,
    AulaMedioIndividual,
    FabricaAula,
)
from app.models.classes.calculadora_salario import CalculadoraSalario, ValeTransporte
from app.models.classes.pessoa import Pessoa
from app.models.classes.portal import PortalAlfabeta
from app.models.classes.professor import Professor


def criar_portal_isolado(tmp_path):
    caminho_prof = tmp_path / "professores.json"
    caminho_aulas = tmp_path / "aulas.json"
    return PortalAlfabeta(
        caminho_professores=str(caminho_prof),
        caminho_aulas=str(caminho_aulas),
    ), caminho_prof, caminho_aulas


def test_heranca_e_polimorfismo():
    assert issubclass(Professor, Pessoa)
    assert issubclass(Aluno, Pessoa)

    prof = Professor("Caua", "caua@email.com", "caua", "123", id=1)
    aluno = Aluno("Arthur")
    assert "Professor" in prof.exibir_identificacao()
    assert "Aluno" in aluno.exibir_identificacao()

    subclasses_esperadas = [
        (AulaFundamentalColetivo, "Fundamental Coletivo", 9.92),
        (AulaFundamentalIndividual, "Fundamental Individual", 16.54),
        (AulaMedioColetivo, "Médio Coletivo", 16.54),
        (AulaMedioIndividual, "Médio Individual", 19.85),
        (AulaFimDeSemana, "Fim de Semana", 37.50),
    ]
    for cls, tipo, valor in subclasses_esperadas:
        assert issubclass(cls, Aula)
        instancia = cls(aluno, "10/11/26", professor=prof)
        assert instancia.tipo_aula == tipo
        assert instancia.calcular_valor() == pytest.approx(valor)


def test_composicao_associacao_e_dependencia(tmp_path):
    portal, _, _ = criar_portal_isolado(tmp_path)
    prof = portal.registrar_professor("Maria", "maria@email.com", "maria", "abc")

    # Composição: Professor cria e possui sua própria AgendaMensal
    assert isinstance(prof.agenda, AgendaMensal)

    # Associação: Aula referencia Aluno e Professor; AgendaMensal guarda as Aulas
    aula1 = portal.adicionar_aula(prof, "João", "10/11/26", "1")  # 9.92
    aula2 = portal.adicionar_aula(prof, "Ana", "10/11/26", "4")   # 19.85 (mesmo dia)
    aula3 = portal.adicionar_aula(prof, "Lucas", "12/11/26", "5") # 37.50

    assert aula1.aluno.nome == "João"
    assert aula1.professor is prof
    assert len(prof.agenda.aulas) == 3

    # Dependência: CalculadoraSalario recebe Professor e ValeTransporte como parâmetros
    vt = ValeTransporte(10.0)
    resumo = CalculadoraSalario.calcular(prof, vale_transporte=vt)
    assert resumo.total_aulas == pytest.approx(9.92 + 19.85 + 37.50)
    assert resumo.dias_trabalhados == 2  # 10/11/26 e 12/11/26
    assert resumo.total_vale_transporte == pytest.approx(20.0)
    assert resumo.total_geral == pytest.approx(87.27)


def test_registro_login_e_validacoes(tmp_path):
    portal, caminho_prof, _ = criar_portal_isolado(tmp_path)

    prof = portal.registrar_professor("Victor", "victor@email.com", "victor", "senha")
    assert prof.id == 1

    with pytest.raises(ValueError):
        portal.registrar_professor("Outro", "o@email.com", "victor", "123")

    with pytest.raises(ValueError):
        portal.registrar_professor("", "a@b.com", "login2", "123")

    assert portal.autenticar("victor", "senha") is prof
    assert portal.autenticar("victor", "errada") is None

    # Verifica persistência no JSON
    dados = json.loads(caminho_prof.read_text(encoding="utf-8"))
    assert len(dados) == 1
    assert dados[0]["login"] == "victor"


def test_alterar_aluno_e_persistencia(tmp_path):
    portal, caminho_prof, caminho_aulas = criar_portal_isolado(tmp_path)
    prof = portal.registrar_professor("Victor", "v@email.com", "victor", "123")

    portal.adicionar_aula(prof, "Carlos", "20/11/26", "1")  # Fundamental Coletivo (9.92)
    portal.adicionar_aula(prof, "Beatriz", "05/11/26", "2") # Fundamental Individual (16.54)

    # Ordenação cronológica coloca 05/11/26 no índice 0 e 20/11/26 no índice 1
    assert portal.listar_aulas(prof)[0].aluno.nome == "Beatriz"

    alterada = portal.alterar_aula(
        professor=prof,
        indice=0,
        novo_nome_aluno="Beatriz Silva",
        nova_data_aula="25/11/26",
        nova_opcao_tipo="5",  # Fim de Semana (37.50)
    )
    assert alterada.aluno.nome == "Beatriz Silva"
    assert alterada.data_aula == "25/11/26"
    assert isinstance(alterada, AulaFimDeSemana)
    assert alterada.calcular_valor() == pytest.approx(37.50)

    # Recarrega do disco para garantir que a alteração foi persistida
    portal_recarregado = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    prof_recarregado = portal_recarregado.autenticar("victor", "123")
    aulas_salvas = portal_recarregado.listar_aulas(prof_recarregado)
    assert [a.aluno.nome for a in aulas_salvas] == ["Carlos", "Beatriz Silva"]
    assert aulas_salvas[1].calcular_valor() == pytest.approx(37.50)


def test_fim_do_mes_persiste_e_isola_professor(tmp_path):
    portal, caminho_prof, caminho_aulas = criar_portal_isolado(tmp_path)
    prof1 = portal.registrar_professor("Ana", "ana@email.com", "ana", "111")
    prof2 = portal.registrar_professor("Bruno", "bruno@email.com", "bruno", "222")

    portal.adicionar_aula(prof1, "Aluno A", "10/11/26", "2")
    portal.adicionar_aula(prof1, "Aluno B", "11/11/26", "3")
    portal.adicionar_aula(prof2, "Aluno C", "12/11/26", "4")

    removidos = portal.finalizar_mes(prof1)
    assert removidos == 2
    assert prof1.agenda.esta_vazia()
    assert len(prof2.agenda.aulas) == 1

    # Recarrega em nova instância e verifica se persistiu no JSON
    portal_recarregado = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    prof1_rec = portal_recarregado.autenticar("ana", "111")
    prof2_rec = portal_recarregado.autenticar("bruno", "222")
    assert prof1_rec.agenda.esta_vazia()
    assert len(prof2_rec.agenda.aulas) == 1
    assert prof2_rec.agenda.aulas[0].aluno.nome == "Aluno C"


def test_fabrica_aula_invalida():
    aluno = Aluno("Teste")
    with pytest.raises(ValueError):
        FabricaAula.criar_por_opcao("99", aluno, "10/11/26")
    with pytest.raises(ValueError):
        FabricaAula.criar_por_tipo("Inexistente", aluno, "10/11/26")


def test_remover_aula_individual_e_persistencia(tmp_path):
    portal, caminho_prof, caminho_aulas = criar_portal_isolado(tmp_path)
    prof = portal.registrar_professor("Victor", "v@email.com", "victor", "123")

    portal.adicionar_aula(prof, "Aluno 1", "05/11/26", "1")
    portal.adicionar_aula(prof, "Aluno 2", "10/11/26", "2")

    removida = portal.remover_aula(prof, 0)
    assert removida.aluno.nome == "Aluno 1"
    assert [a.aluno.nome for a in portal.listar_aulas(prof)] == ["Aluno 2"]

    with pytest.raises(IndexError):
        portal.remover_aula(prof, 5)

    portal_rec = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    prof_rec = portal_rec.autenticar("victor", "123")
    assert [a.aluno.nome for a in portal_rec.listar_aulas(prof_rec)] == ["Aluno 2"]


def test_crud_professor_atualizar_e_remover_em_cascata(tmp_path):
    portal, caminho_prof, caminho_aulas = criar_portal_isolado(tmp_path)
    prof1 = portal.registrar_professor("Ana", "ana@email.com", "ana", "111")
    prof2 = portal.registrar_professor("Bruno", "bruno@email.com", "bruno", "222")

    assert len(portal.listar_professores()) == 2
    assert portal.obter_professor(prof1.id) is prof1
    assert portal.obter_professor(999) is None

    # Falha por login duplicado ou campo vazio não deve deixar estado parcial
    with pytest.raises(ValueError):
        portal.atualizar_professor(prof1, novo_nome="Ana Alterada", novo_login="bruno")
    assert prof1.nome == "Ana"

    with pytest.raises(ValueError):
        portal.atualizar_professor(prof1, novo_nome="Ana Alterada", novo_email="  ")
    assert prof1.nome == "Ana"

    # Atualização válida
    portal.atualizar_professor(
        prof1,
        novo_nome="Ana Paula",
        novo_email="anapaula@email.com",
        novo_login="anapaula",
        nova_senha="999",
    )
    assert portal.autenticar("anapaula", "999") is prof1

    portal.adicionar_aula(prof1, "Aluno Ana", "10/11/26", "1")
    portal.adicionar_aula(prof2, "Aluno Bruno", "11/11/26", "2")

    # Remoção em cascata de prof1 mantém prof2 e suas aulas
    portal.remover_professor(prof1)
    assert portal.obter_professor(prof1.id) is None

    portal_rec = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    assert portal_rec.autenticar("anapaula", "999") is None
    prof2_rec = portal_rec.autenticar("bruno", "222")
    assert prof2_rec is not None
    assert [a.aluno.nome for a in portal_rec.listar_aulas(prof2_rec)] == ["Aluno Bruno"]
