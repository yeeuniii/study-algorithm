from collections import deque


def bfs(graph, start_node):
    visited = list()
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited
