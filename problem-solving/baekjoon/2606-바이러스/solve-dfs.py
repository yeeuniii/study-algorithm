import sys
input = lambda: sys.stdin.readline().strip()


def init_graph(v, e):
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph


def dfs(node, graph, is_visited):
    cnt = 0

    for next_node in graph[node]:
        if next_node not in is_visited:
            is_visited.add(next_node)
            cnt += dfs(next_node, graph, is_visited) + 1
    return cnt


def main():
    v = int(input())
    e = int(input())
    graph = init_graph(v, e)
    result = dfs(1, graph, set())
    print(result - 1 if result else result)


if __name__ == "__main__":
    main()