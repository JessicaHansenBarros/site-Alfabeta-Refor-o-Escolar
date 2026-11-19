# Sistema Alfabeta — Reforço Escolar (Desk App I)

Aplicação de gestão para professores do reforço escolar Alfabeta, estruturada com Programação Orientada a Objetos em Python e persistência em JSON.

## Como executar

```bash
python3 main.py
```

## Como executar os testes

```bash
python3 -m pytest -v
```

## Funcionalidades

- **Cadastro e Login de Professores** com validação de campos obrigatórios e login único (`db/dataBase_professor.json`).
- **Adicionar aluno/aula** escolhendo entre 5 modalidades com valores específicos (`db/dataBase_alunos.json`).
- **Alterar aluno/aula** permitindo atualizar nome do aluno, data da aula e modalidade (recalculando o valor automaticamente e salvando no JSON).
- **Histórico de aulas** ordenado cronologicamente por data, isolado por professor logado.
- **Salário desse mês** somando os valores das aulas do professor com cálculo opcional de vale-transporte por dia único trabalhado.
- **Fim do mês** limpando o histórico do professor logado e persistindo a remoção no arquivo JSON sem afetar outros professores.

## Modelagem Orientada a Objetos e Relações

1. **Herança**:
   - `Pessoa` (`classes/pessoa.py`) é classe base abstrata para `Professor` (`classes/professor.py`) e `Aluno` (`classes/aluno.py`).
   - `Aula` (`classes/aula.py`) é classe base abstrata para `AulaFundamentalColetivo`, `AulaFundamentalIndividual`, `AulaMedioColetivo`, `AulaMedioIndividual` e `AulaFimDeSemana`.
2. **Polimorfismo**:
   - `Pessoa.exibir_identificacao()` é sobrescrito de forma distinta em `Professor` e `Aluno`.
   - `Aula.tipo_aula` e `Aula.calcular_valor()` são sobrescritos nas 5 subclasses de `Aula`, permitindo cálculo uniforme sem condicionais em `CalculadoraSalario`.
3. **Composição**:
   - `Professor` cria e gerencia sua `AgendaMensal` (`self.agenda = AgendaMensal()` em `classes/professor.py`).
   - `PortalAlfabeta` cria e gerencia os repositórios `BancoProfessores` e `BancoAulas` (`classes/portal.py`).
4. **Associação**:
   - `Aula` referencia um `Aluno` (`self.aluno`) e opcionalmente um `Professor` (`self.professor`).
   - `AgendaMensal` mantém a coleção de objetos `Aula` do professor (`classes/agenda.py`).
5. **Dependência**:
   - `CalculadoraSalario.calcular(professor, vale_transporte)` (`classes/calculadora_salario.py`) depende de `Professor`, `ValeTransporte` e `ResumoSalario` apenas via parâmetros e retorno.
   - `FabricaAula` (`classes/aula.py`) e `PortalAlfabeta` (`classes/portal.py`) usam dependências pontuais para instanciar aulas e calcular salários.

## Diagrama UML

- Diagrama em Markdown/Mermaid: [docs/diagrama_uml.md](docs/diagrama_uml.md)
- Diagrama vetorial (SVG): [docs/diagrama_uml.svg](docs/diagrama_uml.svg)
