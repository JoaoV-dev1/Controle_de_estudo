# Controle de Estudos CLI

Versão atual: **1.0.0**

## Descrição do problema real
Muitos estudantes têm dificuldade para manter uma rotina de estudos consistente, registrar o que foi estudado e acompanhar a própria evolução ao longo do tempo. Essa desorganização pode prejudicar o aprendizado, a preparação para provas e a construção de hábitos saudáveis de estudo.

## Proposta da solução
O projeto **Controle de Estudos CLI** é uma aplicação de linha de comando desenvolvida em Python para ajudar estudantes a organizar suas matérias, registrar sessões de estudo e acompanhar o histórico de dedicação por disciplina.

## Público-alvo
- Estudantes do ensino médio
- Estudantes universitários
- Pessoas que estudam para concursos ou certificações

## Funcionalidades principais
- Cadastro de matérias
- Listagem de matérias cadastradas
- Registro de sessões de estudo com duração e observações
- Visualização do histórico de estudos
- Consulta do total de minutos estudados por matéria
- Persistência dos dados em arquivo JSON

## Tecnologias utilizadas
- Python 3.11+
- Pytest
- Ruff
- GitHub Actions
- JSON para armazenamento local

## Estrutura do projeto
```text
controle-estudos/
├── src/
│   ├── main.py
│   └── controle_estudos/
│       ├── __init__.py
│       ├── cli.py
│       ├── core.py
│       └── storage.py
├── tests/
│   └── test_core.py
├── data/
│   └── study_data.json
├── .github/workflows/
│   └── ci.yml
├── pyproject.toml
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Instalação
1. Clone o repositório:
```bash
git clone SEU_LINK_DO_GITHUB
cd controle-estudos
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
```

No Windows:
```bash
.venv\Scripts\activate
```

No Linux/macOS:
```bash
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução
Execute o projeto com:
```bash
python src/main.py
```

## Como usar
Ao iniciar o programa, será exibido um menu com as opções:
- adicionar matéria
- listar matérias
- registrar estudo
- ver histórico
- consultar total por matéria
- sair

Exemplo de uso:
```text
=== Controle de Estudos ===
1 - Adicionar matéria
2 - Listar matérias
3 - Registrar estudo
4 - Ver histórico
5 - Ver total de minutos por matéria
0 - Sair
```

## Executando os testes
```bash
pytest
```

## Executando o lint
```bash
ruff check .
```

## Versionamento semântico
O projeto utiliza versionamento semântico no formato **MAJOR.MINOR.PATCH**.

Versão atual: **1.0.0**

## Autor
João Victor de Sousa Pinto

## Link do repositório público
Substitua este campo após publicar no GitHub:

`SEU_LINK_DO_REPOSITORIO_PUBLICO_AQUI`
