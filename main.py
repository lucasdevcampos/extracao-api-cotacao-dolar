import pandas as pd
import requests
from pathlib import Path

inicial = None
final = None

def datas():
    """Escolher faixa de datas para retorno dos dados."""

    inicial = '01/09/2026'
    final = '15/10/2026'
    return inicial, final

def extrair_dados_api(inicial, final):
    """Acessa API pública do Banco Central para verificar histórico da cotação do Dólar."""
    url = (
        'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?'
        f'formato=json&dataInicial={inicial}&dataFinal={final}'
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    # Se conecta na API utilizando: cabeçalho, limite espera conexão, tratamento erros
    try:
        conexao = requests.get(url, headers=headers, timeout=30)
        conexao.raise_for_status()
    except requests.exceptions.Timeout:
        print("O servidor não está respondendo")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

    # Passando dados de json/api para um dataframe
    dados = pd.DataFrame(conexao.json())
    return dados

def transformar_dados(dados):
    """ Tratamento de tipagem de dados do dataframe """
    dados['valor'] = dados['valor'].astype(float)
    dados['valor'] = dados['valor'].map(lambda x: f"R$ {x:,.2f}")
    return dados

def exportar_dados(dados):
    """ Criar pasta de saída para receber arquivo coletado da api e exportado """
    BASE_DIR = Path(__file__).resolve().parent
    OUT_DIR = BASE_DIR / 'outputs'
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Salva resultado formato xlsx
    dados.to_excel(OUT_DIR / 'historico_dolar.xlsx', index=False)
    return OUT_DIR

def infos(dados, OUT_DIR):
    """ Exibe mensagens no prompt """
    print('=' * 55)
    print(f"-> Histórico de cotação do Dólar")
    print(f" Salvo em .xlsx na pasta: {OUT_DIR.stem} ")
    return dados

if __name__ == '__main__':
    inicial, final = datas()
    dados = extrair_dados_api(inicial, final)
    dados = transformar_dados(dados)
    OUT_DIR = exportar_dados(dados)
    infos(dados, OUT_DIR)