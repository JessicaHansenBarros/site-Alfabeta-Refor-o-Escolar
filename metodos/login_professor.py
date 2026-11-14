from metodos.menu_principal import menu_principal

def login_professor(lista_professores):
    print("\n--- LOGIN DO PROFESSOR ---")

    if not lista_professores:
        print("Nenhum professor cadastrado ainda! Crie uma conta primeiro.")

        return None

    login_digitado = input("Login: ").strip()
    senha_digitada = input("Senha: ").strip()

    for professor in lista_professores:
        if professor.login == login_digitado and professor.senha == senha_digitada:
            print(f"\nBem vindo(a), {professor.nome}!")
            menu_principal(professor)
            return professor

    print("\nErro: Login ou senha incorretos!")
    return None