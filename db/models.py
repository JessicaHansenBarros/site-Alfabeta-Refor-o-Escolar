from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.conexao import Base

class ProfessorDB(Base):
    __tablename__ = "professores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relacionamento: um professor tem vários alunos/aulas
    alunos: Mapped[list["AlunoDB"]] = relationship(back_populates="professor", cascade="all, delete-orphan")


class AlunoDB(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    data_aula: Mapped[str] = mapped_column(String(20), nullable=False)
    tipo_de_aula: Mapped[str] = mapped_column(String(50), nullable=False)
    valor: Mapped[float] = mapped_column(Float, nullable=False)

    # Chave estrangeira ligando ao professor
    id_professor: Mapped[int] = mapped_column(ForeignKey("professores.id"), nullable=False)
    professor: Mapped["ProfessorDB"] = relationship(back_populates="alunos")