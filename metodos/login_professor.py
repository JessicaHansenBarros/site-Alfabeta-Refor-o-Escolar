from metodos.menu_principal import menu_principal
from db.banco_professores import buscar_professor_login

def login_professor():
    print("\n--- LOGIN DO PROFESSOR ---")

    login_digitado = input("Login: ").strip()
    senha_digitada = input("Senha: ").strip()
      
    professor = buscar_professor_login(login_digitado, senha_digitada)

    if professor:
        print(f"\nBem vindo(a), {professor.nome}!")
        menu_principal(professor)
        return professor

    print("\nErro: Login ou senha incorretos!")
    return None