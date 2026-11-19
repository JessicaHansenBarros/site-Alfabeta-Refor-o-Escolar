# Diagrama UML — Sistema Alfabeta Reforço Escolar

Este diagrama representa a modelagem completa Orientada a Objetos do sistema, contemplando **Herança**, **Polimorfismo**, **Composição**, **Associação** e **Dependência**.

```mermaid
classDiagram
    direction TB

    class Pessoa {
        <<abstract>>
        +nome: str
        +exibir_identificacao()* str
    }

    class Aluno {
        +exibir_identificacao() str
    }

    class Professor {
        +id: int | None
        +email: str
        +login: str
        +senha: str
        +agenda: AgendaMensal
        +exibir_identificacao() str
        +adicionar_aula(aula: Aula) void
        +to_dict() dict
        +from_dict(dados: dict) Professor
    }

    class AgendaMensal {
        -_aulas: list~Aula~
        +aulas: list~Aula~
        +esta_vazia() bool
        +ordenar() void
        +adicionar(aula: Aula) void
        +substituir(indice: int, nova_aula: Aula) void
        +obter(indice: int) Aula
        +limpar() void
        +dias_trabalhados() set~str~
    }

    class Aula {
        <<abstract>>
        +aluno: Aluno
        +data_aula: str
        +professor: Professor | None
        +id_professor: int | None
        +tipo_aula()* str
        +calcular_valor()* float
        +descrever() str
        +to_dict() dict
    }

    class AulaFundamentalColetivo {
        +tipo_aula() str
        +calcular_valor() float
    }

    class AulaFundamentalIndividual {
        +tipo_aula() str
        +calcular_valor() float
    }

    class AulaMedioColetivo {
        +tipo_aula() str
        +calcular_valor() float
    }

    class AulaMedioIndividual {
        +tipo_aula() str
        +calcular_valor() float
    }

    class AulaFimDeSemana {
        +tipo_aula() str
        +calcular_valor() float
    }

    class FabricaAula {
        +OPCOES: dict
        +POR_TIPO: dict
        +listar_opcoes() list
        +criar_por_opcao(opcao, aluno, data_aula, professor) Aula
        +criar_por_tipo(tipo_aula, aluno, data_aula, professor) Aula
        +from_dict(dados, professor) Aula
    }

    class ValeTransporte {
        +valor_diario: float
        +calcular_total(dias_trabalhados: int) float
    }

    class ResumoSalario {
        +total_aulas: float
        +dias_trabalhados: int
        +total_vale_transporte: float
        +total_geral: float
    }

    class CalculadoraSalario {
        +calcular(professor: Professor, vale_transporte: ValeTransporte) ResumoSalario
    }

    class BancoProfessores {
        +caminho: str
        +carregar() list~Professor~
        +salvar(lista_professores: list~Professor~) void
    }

    class BancoAulas {
        +caminho: str
        +carregar(professores_por_id: dict) list~Aula~
        +salvar(lista_aulas: list~Aula~) void
    }

    class PortalAlfabeta {
        +banco_professores: BancoProfessores
        +banco_aulas: BancoAulas
        +professores: list~Professor~
        +aulas: list~Aula~
        +registrar_professor(nome, email, login, senha) Professor
        +autenticar(login, senha) Professor | None
        +adicionar_aula(professor, nome_aluno, data_aula, opcao_tipo) Aula
        +alterar_aula(professor, indice, novo_nome_aluno, nova_data_aula, nova_opcao_tipo) Aula
        +listar_aulas(professor) list~Aula~
        +calcular_salario(professor, valor_vale_diario) ResumoSalario
        +finalizar_mes(professor) int
    }

    %% Herança (e Polimorfismo via métodos sobrescritos)
    Pessoa <|-- Aluno : Herança
    Pessoa <|-- Professor : Herança
    Aula <|-- AulaFundamentalColetivo : Herança
    Aula <|-- AulaFundamentalIndividual : Herança
    Aula <|-- AulaMedioColetivo : Herança
    Aula <|-- AulaMedioIndividual : Herança
    Aula <|-- AulaFimDeSemana : Herança

    %% Composição
    Professor *-- "1" AgendaMensal : Composição
    PortalAlfabeta *-- "1" BancoProfessores : Composição
    PortalAlfabeta *-- "1" BancoAulas : Composição

    %% Associação
    AgendaMensal "1" o-- "0..*" Aula : Associação
    Aula "0..*" --> "1" Aluno : Associação
    Aula "0..*" --> "0..1" Professor : Associação
    PortalAlfabeta "1" --> "0..*" Professor : Associação
    PortalAlfabeta "1" --> "0..*" Aula : Associação

    %% Dependência
    CalculadoraSalario ..> Professor : Dependência
    CalculadoraSalario ..> ValeTransporte : Dependência
    CalculadoraSalario ..> ResumoSalario : Dependência
    PortalAlfabeta ..> CalculadoraSalario : Dependência
    PortalAlfabeta ..> FabricaAula : Dependência
    FabricaAula ..> Aula : Dependência
    FabricaAula ..> Aluno : Dependência
```

Visualização vetorial disponível também em [diagrama_uml.svg](./diagrama_uml.svg).
