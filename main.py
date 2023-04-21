from dados.baixar_dados import download_dados
from matrizes.criar_matriz import criar_matriz
from algoritmo.kruskal import Grafo
# from desenhar.desenha_grafo import desenha_grafo

def menu() -> str:
    opcoes = {
        1: "sh07",
        2: "sp11",
        3: "uk12",
        4: "lau15",
        5: "wg22",
        6: "wg59",
        7: "sgb128",
        0: "sair"
    }

    for k, v in opcoes.items():
        print(f"[{k}] - {v.upper()}")
    
    escolha = int(input("Digite uma opção: "))

    if escolha in opcoes:
        return opcoes[escolha]
    
    print("Opção inválida. Por favor, digite um número válido de opção.\n")
    return menu()


def main():
    escolha = menu()

    while escolha != "sair":
        print(f"\nVocê escolheu {escolha.upper()}.\n")
        
        dados = download_dados(f"https://people.sc.fsu.edu/~jburkardt/datasets/cities/{escolha}_dist.txt")
        matriz = criar_matriz(dados)
        grafo = Grafo(len(matriz))

        # Inicializa listas para armazenar as arestas, pesos e vértices
        # edges = []
        # weights = []
        # vertices = [str(i) for i in range(len(matriz))]

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                # Adiciona apenas as arestas que estão na parte superior da matriz
                # (para evitar adicionar arestas duplicadas)
                if j > i:
                    grafo.adicionar_aresta(i, j, matriz[i][j])
                    # edges.append((i, j))
                    # weights.append(round(matriz[i][j]))
        
        grafo.kruskal_mst()
        grafo.ver_mst()

        # Plota o gráfico
        # desenha_grafo(escolha.upper(), edges, len(matriz), weights, vertices)
        
        escolha = menu()

main()
