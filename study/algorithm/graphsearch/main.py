from study.algorithm.graphsearch.bfs import bfs
from study.algorithm.graphsearch.dfs import dfs

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

print("bfs : ", bfs(graph, 'A'))
print("dfs : ", dfs(graph, 'A'))
