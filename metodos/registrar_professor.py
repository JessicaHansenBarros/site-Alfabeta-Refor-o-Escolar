from sqlalchemy.exc import IntegrityError
from db.banco_professores import salvar_professor


def registrar_professor():
    print("\n--REGISTRO DE NOVO PROFESSOR--\n")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    try:
        salvar_professor(nome, email, login, senha)
        print("Conta criada e salva com sucesso!\n")
    except IntegrityError:
        print("\nErro: Já existe um professor cadastrado com este email ou login!\n")