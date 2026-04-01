def backtrack(graph, current, result):
    for header in graph.get(current, []):
        # avoid revisiting nodes already in result
        if header in result:
            continue
        result.append(header)
        print(header)
        if header in graph:
            backtrack(graph, header, result)
def DFS(graph, current):
    result = []
    print("Depth First Search")
    print("------------------------------")
    print(current)
    result.append(current)
    backtrack(graph, current, result)
    print("------------------------------")
    return result

def DFS_gui(graph, head, callback):
    result = []
    result = DFS(graph, head)
    callback(result)
    return result
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