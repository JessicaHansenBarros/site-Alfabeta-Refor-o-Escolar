from db.conexao import SessionLocal
from db.models import ProfessorDB

def salvar_professor(nome, email, login, senha):
    with SessionLocal() as session:
        novo_prof = ProfessorDB(nome=nome, email=email, login=login, senha=senha)
        session.add(novo_prof)
        session.commit()
        session.refresh(novo_prof)  # Atualiza com o ID gerado pelo banco
        return novo_prof

def buscar_professor_login(login, senha):
    with SessionLocal() as session:
        return session.query(ProfessorDB).filter_by(login=login, senha=senha).first()