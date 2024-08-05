# 무방향 그래프
def make_undirected_graph_by_adjacency_matrix(v, m, edge):
    adj = list([0] * (v + 1) for _ in range(v + 1))

    for idx in range(m):
        i = edge[2 * idx]
        j = edge[2 * idx + 1]

        adj[i][j] = 1
        adj[j][i] = 1

    return adj


# 방향 그래프
def make_directed_graph_by_adjacency_matrix(v, m, edge):
    adj = list([0] * (v + 1) for _ in range(v + 1))

    for idx in range(m):
        i = edge[2 * idx]
        j = edge[2 * idx + 1]

        adj[i][j] = 1

    return adj


def print_graph(graph):
    for idx, line in enumerate(graph):
        if idx:
            print(line)


def main():
    number_of_vertex = 6
    number_of_edge = 8
    edges = [1, 2, 1, 3, 1, 4, 1, 6, 2, 4, 3, 5, 3, 6, 4, 6]

    print("무방향 그래프")
    print_graph(make_undirected_graph_by_adjacency_matrix(number_of_vertex, number_of_edge, edges))
    print("-" * 25)
    print("방향 그래프")
    print_graph(make_directed_graph_by_adjacency_matrix(number_of_vertex, number_of_edge, edges))


if __name__ == "__main__":
    main()