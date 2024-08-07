import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()


def init_graph(v, e):
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs(graph):
    queue = deque([1])
    is_visited = set()

    while queue:
        node = queue.popleft()
        if node not in is_visited:
            is_visited.add(node)
            queue.extend(graph[node])
    return len(is_visited) - 1


def main():
    v = int(input())
    e = int(input())
    graph = init_graph(v, e)
    print(bfs(graph))


if __name__ == "__main__":
    main()