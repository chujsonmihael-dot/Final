def backtrack(graph, current):
    for header in graph[current]:
        print(header)
        if header in graph:
            backtrack(graph, header)
def DFS(graph, current):
    print("Depth First Search")
    print("------------------------------")
    print(current)
    backtrack(graph, current)
    print("------------------------------")
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