def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited
