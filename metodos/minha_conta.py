from app.models.classes.portal import PortalAlfabeta
from app.models.classes.professor import Professor


def gerenciar_conta(portal: PortalAlfabeta, professor: Professor) -> bool:
    """
    Exibe, atualiza ou exclui a conta do professor logado.
    Retorna True se a conta foi excluída (encerrando a sessão).
    """
    while True:
        aulas = portal.listar_aulas(professor)
        print("\n--- MINHA CONTA ---")
        print(f"ID: {professor.id}")
        print(f"Nome: {professor.nome}")
        print(f"Email: {professor.email}")
        print(f"Login: {professor.login}")
        print(f"Aulas na agenda: {len(aulas)}")
        print("\n1: Atualizar dados da conta")
        print("2: Excluir minha conta")
        print("3: Voltar")

        opcao = input("Escolha (1, 2 ou 3): ").strip()

        if opcao == "1":
            print("\n(Deixe em branco e pressione Enter para manter o valor atual.)")
            novo_nome = input(f"Novo nome [{professor.nome}]: ")
            novo_email = input(f"Novo email [{professor.email}]: ")
            novo_login = input(f"Novo login [{professor.login}]: ")
            nova_senha = input("Nova senha [manter atual]: ")

            try:
                portal.atualizar_professor(
                    professor=professor,
                    novo_nome=novo_nome if novo_nome.strip() else None,
                    novo_email=novo_email if novo_email.strip() else None,
                    novo_login=novo_login if novo_login.strip() else None,
                    nova_senha=nova_senha if nova_senha.strip() else None,
                )
                print("\nDados da conta atualizados com sucesso!")
            except ValueError as erro:
                print(f"Erro ao atualizar conta: {erro}")

        elif opcao == "2":
            confirmacao = input(
                "Tem certeza que deseja excluir permanentemente sua conta e suas aulas? (1: Sim | 2: Não): "
            ).strip()
            if confirmacao == "1":
                portal.remover_professor(professor)
                print("\nConta excluída com sucesso!")
                return True
            print("Exclusão cancelada.")

        elif opcao == "3":
            return False

        else:
            print("Opção inválida! Digite 1, 2 ou 3.")
