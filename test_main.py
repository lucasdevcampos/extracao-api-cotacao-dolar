from main import datas, transformar_dados
import pandas as pd


def test_datas_retorna_strings():
  """datas() deve retornar strings no formato DD/MM/AAAA."""
  resultado = datas()

  assert isinstance(resultado, tuple)
  assert len(resultado) == 2
  assert resultado[0] == '01/09/2026'
  assert resultado[1] == '15/10/2026'

def test_transformar_dados():
  """transformar_dados deve converter 'valor' para float e formatar com R$ x.xx."""
  df = pd.DataFrame({
    'data': ['01/09/2026', '15/10/2026'],
    'valor': ['5.10','5.25']
  })

  resultado = transformar_dados(df)

  assert resultado['valor'].iloc[0] == 'R$ 5.10'
  assert resultado['valor'].iloc[1] == 'R$ 5.25'