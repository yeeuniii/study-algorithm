from collections import defaultdict


def make_undirected_graph_by_adjacency_list(v, e, edge):
    adj = defaultdict(list)
    # adj = list(list() for _ in range(v + 1))

    for idx in range(e):
        i = edge[2 * idx]
        j = edge[2 * idx + 1]

        adj[i].append(j)
        adj[j].append(i)

    return adj


def make_directed_graph_by_adjacency_list(v, e, edge):
    adj = defaultdict(list)
    # adj = list(list() for _ in range(v + 1))

    for idx in range(e):
        i = edge[2 * idx]
        j = edge[2 * idx + 1]

        adj[i].append(j)

    return adj


def print_graph(graph):
    for key in graph.keys():
        print(key, ":", graph[key])


def main():
    number_of_vertex = 6
    number_of_edge = 8
    edges = [1, 2, 1, 3, 1, 4, 1, 6, 2, 4, 3, 5, 3, 6, 4, 6]

    print("무방향 그래프")
    print_graph(make_undirected_graph_by_adjacency_list(number_of_vertex, number_of_edge, edges))
    print("-" * 25)
    print("방향 그래프")
    print_graph(make_directed_graph_by_adjacency_list(number_of_vertex, number_of_edge, edges))


if __name__ == "__main__":
    main()