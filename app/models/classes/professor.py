from app.models.classes.agenda import AgendaMensal
from app.models.classes.aula import Aula
from app.models.classes.pessoa import Pessoa


class Professor(Pessoa):
    """Representa um professor do reforço escolar e compõe sua AgendaMensal."""

    def __init__(
        self,
        nome: str,
        email: str,
        login: str,
        senha: str,
        id: int | None = None,
    ):
        super().__init__(nome)
        self.id = id
        self.email = email.strip()
        self.login = login.strip()
        self.senha = senha.strip()
        # Composição: a AgendaMensal nasce com o Professor e pertence a ele
        self.agenda = AgendaMensal()

    def exibir_identificacao(self) -> str:
        return f"Professor(a): {self.nome} | Email: {self.email}"

    def adicionar_aula(self, aula: Aula) -> None:
        aula.professor = self
        self.agenda.adicionar(aula)

    def atualizar_dados(
        self,
        nome: str | None = None,
        email: str | None = None,
        login: str | None = None,
        senha: str | None = None,
    ) -> None:
        """Valida todos os campos informados antes de atualizar os dados do professor."""
        nome_final = self.nome
        if nome is not None:
            nome_final = nome.strip()
            if not nome_final:
                raise ValueError("O nome não pode ficar vazio.")

        email_final = self.email
        if email is not None:
            email_final = email.strip()
            if not email_final:
                raise ValueError("O email não pode ficar vazio.")

        login_final = self.login
        if login is not None:
            login_final = login.strip()
            if not login_final:
                raise ValueError("O login não pode ficar vazio.")

        senha_final = self.senha
        if senha is not None and senha.strip():
            senha_final = senha.strip()

        self.nome = nome_final
        self.email = email_final
        self.login = login_final
        self.senha = senha_final

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "login": self.login,
            "senha": self.senha,
        }

    @classmethod
    def from_dict(cls, dados: dict) -> "Professor":
        return cls(
            nome=dados["nome"],
            email=dados["email"],
            login=dados["login"],
            senha=dados["senha"],
            id=dados.get("id"),
        )
