from dataclasses import dataclass
from aluno import aluno
@dataclass

class AlunoFundamentalColetivo(aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAaula = "Fundamental Coletivo"
        self.valor = 9.92

class AlunoFundamentalIndividual(aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAaula = "Fundamental Individual"
        self.valor = 16.54

class AlunoMedioColetivo(aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAaula = "Médio Coletivo"
        self.valor = 16.54

class AlunoMedioIndividual(aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAaula = "Médio Individual"
        self.valor = 19.85

class AlunoFimDeSemana(aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAaula = "Fim de Semana"
        self.valor = 37.50

