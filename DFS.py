


def DFS(graph, current, visited):
    print(current)
    for newHead in graph[current]:
        if newHead not in visited:
            visited.add(newHead)
            DFS(graph, newHead, visited)
    return "Done"

if __name__ == "__main__":
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
    visited = set()
    current = "A"
    DFS(graph, current, visited)