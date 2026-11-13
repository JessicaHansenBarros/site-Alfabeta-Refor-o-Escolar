from dataclasses import dataclass
from classes.aluno import Aluno
@dataclass

class AlunoFundamentalColetivo(Aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAula = "Fundamental Coletivo"
        self.valor = 9.92

class AlunoFundamentalIndividual(Aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAula = "Fundamental Individual"
        self.valor = 16.54

class AlunoMedioColetivo(Aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAula = "Médio Coletivo"
        self.valor = 16.54

class AlunoMedioIndividual(Aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAula = "Médio Individual"
        self.valor = 19.85

class AlunoFimDeSemana(Aluno):
    def __init__(self, nome, data_aula):
        super().__init__(nome, data_aula)
        self.TipoDeAula = "Fim de Semana"
        self.valor = 37.50

