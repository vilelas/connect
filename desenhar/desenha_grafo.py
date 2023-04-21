import igraph

# Função para plotar um grafo
def desenha_grafo(graph_name, edge_list, vertex_count, weight_list, label_list):
    # Cria um grafo não-direcionado
    g = igraph.Graph(directed=False)

    # Adiciona os vértices ao grafo
    g.add_vertices(vertex_count)

    # Adiciona as arestas ao grafo
    g.add_edges(edge_list)

    # Atribui os pesos às arestas
    g.es["weight"] = weight_list

    # Cria o estilo visual do grafo
    visual_style = {}

    # Atribui os rótulos aos vértices
    visual_style["vertex_label"] = label_list

    # Atribui cor aos vértices
    visual_style["vertex_color"] = "white"

    # Atribui os pesos às arestas
    visual_style["edge_label"] = weight_list

    # Plota o grafo em um arquivo de imagem
    igraph.plot(g, f"{graph_name}.png", **visual_style)