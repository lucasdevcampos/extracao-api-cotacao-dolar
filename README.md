# Extração de Cotação do Dólar (API do Banco Central)

[![Tests](https://github.com/lucasdevcampos/extracao-api-cotacao-dolar/actions/workflows/tests.yml/badge.svg)]

Script em Python que consulta a API pública do Banco Central (SGS 1) e exporta
o histórico da cotação do Dólar (PTAX) em uma planilha `.xlsx`.

## Como funciona

- `datas()` — define o período da consulta (datas `inicial` e `final`). Edite esta função para mudar o intervalo.
- `extrair_dados_api(inicial, final)` — monta a URL da API do BCB, faz a requisição com `requests` (timeout de 30s, User-Agent e tratamento de erro) e retorna um `DataFrame`.
- `transformar_dados(dados)` — converte a coluna `valor` para `float` e formata como `R$ X.XX`.
- `exportar_dados(dados)` — cria a pasta `outputs/` e salva `historico_dolar.xlsx`.
- `infos(dados, OUT_DIR)` — imprime no terminal o resumo e o caminho do arquivo salvo.

## Como rodar

### Pré-requisitos

- Python 3.10 ou superior
- Git

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/lucasdevcampos/extracao-api-cotacao-dolar.git
cd extracao-api-cotacao-dolar
```

2. Crie e ative um ambiente virtual:

**Windows (Git Bash):**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

**Mac/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

O script consulta a API, imprime um resumo no terminal e salva o resultado em
`outputs/historico_dolar.xlsx`.

Para mudar o período consultado, edite a função `datas()` no `main.py`
(variáveis `inicial` e `final`).

### Testes

```bash
pytest -v
```

Saída esperada: `2 passed`.

## Entrada

Nenhuma entrada de arquivo. O script consulta diretamente a API do Banco Central:

- Endpoint: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados`
- Série: `bcdata.sgs.1` (cotação do Dólar — PTAX)
- Período: definido em `datas()` (padrão: `01/09/2026` a `15/10/2026`)

## Saída

Planilha `outputs/historico_dolar.xlsx` com as colunas retornadas pela API:

- `data` — data da cotação
- `valor` — valor formatado como `R$ X.XX`

## Autor

Lucas Campos — [@lucasdevcampos](https://github.com/lucasdevcampos)

## Licença

MIT