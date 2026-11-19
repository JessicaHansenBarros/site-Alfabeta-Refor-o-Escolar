from classes.portal import PortalAlfabeta
from metodos.menu_inicial import menu_inicial


def executar_com_entradas(monkeypatch, entradas):
    iterador = iter(entradas)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(iterador))


def test_fluxo_completo_cli(tmp_path, monkeypatch, capsys):
    caminho_prof = tmp_path / "professores.json"
    caminho_aulas = tmp_path / "aulas.json"
    portal = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))

    # 1. Cadastra professor -> 2. Faz login -> 1. Adiciona aula ->
    # 3. Altera aula -> 4. Exibe histórico -> 2. Calcula salário (com VT) ->
    # 5. Fim do mês (confirma) -> 6. Desloga -> 3. Sair
    entradas = [
        "1", "Victor Silva", "victor@email.com", "victor", "1234",
        "2", "victor", "1234",
        "1", "Pedro", "15/11/26", "2",          # Fundamental Individual: 16.54
        "3", "1", "Pedro Henrique", "", "4",    # Altera para Médio Individual: 19.85
        "4",                                    # Histórico
        "2", "1", "10,00",                      # Salário com VT 10.00 (1 dia -> 29.85)
        "5", "1",                               # Fim do mês -> Sim
        "6",                                    # Deslogar
        "3",                                    # Sair
    ]
    executar_com_entradas(monkeypatch, entradas)

    menu_inicial(portal)
    saida = capsys.readouterr().out

    assert "Conta criada e salva com sucesso!" in saida
    assert "Bem-vindo(a), Victor Silva!" in saida
    assert "Pedro Henrique" in saida
    assert "Médio Individual" in saida
    assert "R$ 29.85" in saida
    assert "Histórico de alunos deletado e salvo com sucesso! (1 registro(s) removido(s))" in saida
    assert "Encerrando..." in saida

    # Garante que a limpeza do fim do mês foi persistida no JSON
    portal_novo = PortalAlfabeta(str(caminho_prof), str(caminho_aulas))
    prof = portal_novo.autenticar("victor", "1234")
    assert prof is not None
    assert prof.agenda.esta_vazia()
