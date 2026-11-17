from db.conexao import SessionLocal
from db.models import AlunoDB

def salvar_aluno(nome, data_aula, tipo_de_aula, valor, id_professor):
    with SessionLocal() as session:
        novo_aluno = AlunoDB(
            nome=nome,
            data_aula=data_aula,
            tipo_de_aula=tipo_de_aula,
            valor=valor,
            id_professor=id_professor
        )
        session.add(novo_aluno)
        session.commit()
        session.refresh(novo_aluno)
        return novo_aluno

def listar_alunos_do_professor(id_professor):
    with SessionLocal() as session:
        return (
            session.query(AlunoDB)
            .filter_by(id_professor=id_professor)
            .order_by(AlunoDB.data_aula)
            .all()
        )

def limpar_alunos_do_professor(id_professor):
    with SessionLocal() as session:
        session.query(AlunoDB).filter_by(id_professor=id_professor).delete()
        session.commit()
     
