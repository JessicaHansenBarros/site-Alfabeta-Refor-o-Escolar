# Sistema Alfabeta — Reforço Escolar (BMVC + CLI)

Aplicação de gestão para professores do reforço escolar Alfabeta, integrando a arquitetura Web **BMVC (Bottle)** e a interface **Terminal (CLI)** sobre uma única camada de domínio Orientada a Objetos e persistência em JSON.

## Como executar

### 1. Aplicação Web (BMVC / Bottle)
```bash
python3 route.py
```
Acesse no navegador: `http://localhost:8080/portal` (e `http://localhost:8080/cadastro` para registrar novos professores).

### 2. Via Docker (BMVC)
```bash
docker build -t bmvci .
docker run -d -p 8080:8080 -v $(pwd):/bmeta bmvci
```

### 3. Aplicação Terminal (CLI)
```bash
python3 main.py
```

## Como executar os testes

```bash
python3 -m pytest -v
```

## Arquitetura BMVC e Estrutura do Projeto

- `route.py`: ponto de entrada Web (Bottle) com rotas `/`, `/portal`, `/cadastro`, `/portal/adicionar`, `/portal/salario`, `/portal/alterar`, `/portal/excluir`, `/portal/perfil`, `/portal/perfil/atualizar`, `/portal/perfil/excluir`, `/portal/fim-do-mes`, `/sair`, `/helper` e `/static/<filepath:path>`.
- `app/controllers/application.py`: controlador `Application` do padrão BMVC.
- `app/controllers/db/`: repositórios `BancoProfessores` e `BancoAulas` com os bancos JSON (`dataBase_professor.json` e `dataBase_alunos.json`).
- `app/models/classes/`: camada única de domínio Orientada a Objetos compartilhada entre Web e CLI.
- `app/views/html/` e `app/static/`: templates HTML/TPL (`login.html`, `cadastro.html`, `portal.html`, `helper.tpl`), CSS, JS e imagens.
- `main.py` e `metodos/`: ponto de entrada e adaptadores de menu para execução via terminal (CLI).

## Funcionalidades

- **CRUD completo de Professores (Minha Conta)** com cadastro, login, visualização, atualização cadastral e exclusão de conta com limpeza em cascata das aulas vinculadas (`app/controllers/db/dataBase_professor.json`), disponíveis na Web e no CLI.
- **Adicionar aluno/aula** escolhendo entre 5 modalidades com valores específicos (`app/controllers/db/dataBase_alunos.json`).
- **Alterar aluno/aula** permitindo atualizar nome do aluno, data da aula e modalidade (recalculando o valor automaticamente e salvando no JSON).
- **Excluir aluno/aula** permitindo remover registros individuais (por aba dedicada ou diretamente na tabela na Web, e via menu no CLI) sem afetar o restante da agenda.
- **Histórico de aulas** ordenado cronologicamente por data, isolado por professor logado.
- **Salário desse mês** somando os valores das aulas do professor com cálculo opcional de vale-transporte por dia único trabalhado.
- **Fim do mês** limpando o histórico do professor logado e persistindo a remoção no arquivo JSON sem afetar outros professores.

## Modelagem Orientada a Objetos e Relações

1. **Herança**:
   - `Pessoa` (`app/models/classes/pessoa.py`) é classe base abstrata para `Professor` (`app/models/classes/professor.py`) e `Aluno` (`app/models/classes/aluno.py`).
   - `Aula` (`app/models/classes/aula.py`) é classe base abstrata para `AulaFundamentalColetivo`, `AulaFundamentalIndividual`, `AulaMedioColetivo`, `AulaMedioIndividual` e `AulaFimDeSemana`.
2. **Polimorfismo**:
   - `Pessoa.exibir_identificacao()` é sobrescrito de forma distinta em `Professor` e `Aluno`.
   - `Aula.tipo_aula` e `Aula.calcular_valor()` são sobrescritos nas 5 subclasses de `Aula`, permitindo cálculo uniforme sem condicionais em `CalculadoraSalario`.
3. **Composição**:
   - `Professor` cria e gerencia sua `AgendaMensal` (`self.agenda = AgendaMensal()` em `app/models/classes/professor.py`).
   - `PortalAlfabeta` cria e gerencia os repositórios `BancoProfessores` e `BancoAulas` (`app/models/classes/portal.py`).
4. **Associação**:
   - `Aula` referencia um `Aluno` (`self.aluno`) e opcionalmente um `Professor` (`self.professor`).
   - `AgendaMensal` mantém a coleção de objetos `Aula` do professor (`app/models/classes/agenda.py`).
   - `Application` (`app/controllers/application.py`) associa-se ao `PortalAlfabeta` e ao `current_user` (`Professor`).
5. **Dependência**:
   - `CalculadoraSalario.calcular(professor, vale_transporte)` (`app/models/classes/calculadora_salario.py`) depende de `Professor`, `ValeTransporte` e `ResumoSalario` apenas via parâmetros e retorno.
   - `FabricaAula` (`app/models/classes/aula.py`) e `PortalAlfabeta` (`app/models/classes/portal.py`) usam dependências pontuais para instanciar aulas e calcular salários.

## Diagrama UML

- Diagrama em Markdown/Mermaid: [docs/diagrama_uml.md](docs/diagrama_uml.md)
- Diagrama vetorial (SVG): [docs/diagrama_uml.svg](docs/diagrama_uml.svg)
