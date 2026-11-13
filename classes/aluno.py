from dataclasses import dataclass
@dataclass

class Aluno:
    def __init__(self, nome, data_aula, id_professor=None):
        self.nome = nome    
        self.data_aula = data_aula 
        self.id_professor = id_professor
        self.TipoDeAula = ""
        self.valor = 0.0


    def to_dict(self):
        
        return{
            "nome": self.nome,
            "data_aula": self.data_aula,
            "id_professor": self.id_professor,
            "tipo_de_aula": self.TipoDeAula,
            "valor": self.valor
        }

    @classmethod
    def from_dict(cls, dados_aluno: dict):
        from classes.Valores import (
            AlunoFundamentalColetivo,
            AlunoFundamentalIndividual,
            AlunoMedioColetivo,
            AlunoMedioIndividual,
            AlunoFimDeSemana
        )

        mapa_classes = {
            "Fundamental Coletivo": AlunoFundamentalColetivo,
            "Fundamental Individual": AlunoFundamentalIndividual,
            "Médio Coletivo": AlunoMedioColetivo,
            "Médio Individual": AlunoMedioIndividual,
            "Fim de Semana": AlunoFimDeSemana
        }
        tipo = dados_aluno.get("tipo_de_aula")
        classe_especifica = mapa_classes.get(tipo, cls)
        
        aluno_obj = classe_especifica(dados_aluno["nome"], dados_aluno["data_aula"])
        aluno_obj.id_professor = dados_aluno.get("id_professor")
        return aluno_obj

       
