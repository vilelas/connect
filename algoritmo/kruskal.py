class Grafo:
    def __init__(self, num_vertices):
        # Número de vértices do grafo
        self.num_vertices = num_vertices
        self.resultado = [] 

        # Lista de arestas do grafo
        self.arestas = []

    # Adiciona uma aresta ao grafo
    def adicionar_aresta(self, u, v, w):
        self.arestas.append([u, v, w])

    # Encontra o conjunto de um elemento i
    # (utiliza técnica de compressão de caminho)
    def encontrar(self, pai, i):
        if pai[i] == i:
            return i
        return self.encontrar(pai, pai[i])

    # Realiza a união de dois conjuntos de x e y
    # (utiliza união por classificação)
    def unir(self, pai, classificacao, x, y):
        raiz_x = self.encontrar(pai, x)
        raiz_y = self.encontrar(pai, y)

        # Anexa a árvore de menor classificação sob a raiz da
        # árvore de alta classificação (união por classificação)
        if classificacao[raiz_x] < classificacao[raiz_y]:
            pai[raiz_x] = raiz_y
        elif classificacao[raiz_x] > classificacao[raiz_y]:
            pai[raiz_y] = raiz_x

        # Se as classificações são iguais, então faz com que um seja raiz
        # e incrementa sua classificação em um
        else:
            pai[raiz_y] = raiz_x
            classificacao[raiz_x] += 1

    # Constroi a MST utilizando o algoritmo de Kruskal
    def kruskal_mst(self):
        # Ordena as arestas pelo seu peso
        self.arestas = sorted(self.arestas, key=lambda aresta: aresta[2])

        # Inicializa a lista de pais e a lista de ranques com valores iniciais
        pai = list(range(self.num_vertices))
        classificacao = [0] * self.num_vertices

        e = 0  # Contador de arestas selecionadas
        i = 0  # Índice da aresta atual

        # Enquanto ainda não selecionamos todas as arestas
        while e < self.num_vertices - 1:
            # Pega a próxima aresta
            u, v, w = self.arestas[i]
            i += 1

            # Encontra os pais de cada vértice da aresta
            x = self.encontrar(pai, u)
            y = self.encontrar(pai, v)

            # Se os pais forem diferentes, significa que a aresta não forma um ciclo
            # então adicionamos à MST e unimos os conjuntos de vértices
            if x != y:
                e += 1
                self.resultado.append([u, v, w])
                self.unir(pai, classificacao, x, y)

    def ver_mst(self):
        custo_minimo = 0
        print("A seguir estão as arestas da MST gerada:")
        for aresta in self.resultado:
            u, v, peso = aresta
            custo_minimo += peso
            print(f"{u} -- {v} == {peso}")
        print(f"O Peso da árvore geradora mínima é: {custo_minimo}\n")