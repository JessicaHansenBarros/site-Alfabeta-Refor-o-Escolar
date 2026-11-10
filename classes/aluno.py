from dataclasses import dataclass
@dataclass

class Aluno:
    def __init__(self, nome, data_aula):
        self.nome = nome    
        self.data_aula = data_aula    
