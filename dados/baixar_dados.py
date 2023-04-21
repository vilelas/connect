import requests

def download_dados(url: str) -> str:
    """
    Faz o download de dados de uma URL e retorna o texto.

    Args:
    url (str): A URL do arquivo de dados.

    Returns:
    str: O texto dos dados baixados.
    """
    return requests.get(url).text

