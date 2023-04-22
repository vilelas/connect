def criar_matriz(data: str) -> list:
    """
    Cria uma matriz a partir de uma string contendo os valores em formato de tabela.
    
    Args:
    data (str): A string contendo os valores da matriz em formato de tabela.
    
    Returns:
    matriz (list): A matriz criada a partir dos valores da string.
    """
    
    # Inicializa a lista vazia para armazenar a matriz
    matriz = []
    
    # Itera sobre cada linha do texto recebido
    for linha in data.split("\n"):
        # Separa os valores da linha em uma lista
        valores = linha.split()
        
        # Verifica se a linha não está vazia e não começa com #
        if valores and not "#" in valores[0]:
            # Converte os valores para float e adiciona na lista da matriz
            linha_convertida = list(map(float, valores))
            matriz.append(linha_convertida)
    
    return matriz