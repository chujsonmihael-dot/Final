def DFS(graph, current):
    for header in graph[current]:
        print(header)
        DFS(graph, header)

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    DFS(graph, "A")