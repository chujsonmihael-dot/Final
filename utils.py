def graph_maker():
    graph = {}
    head = ""
    print("GRAPH CREATOR")
    print("------------------------------")
    while True:
        print("Your graph is:")
        print(graph)
        print("------------------------------")
        print("Type a char, and its children after")
        print("Example: <AJC> --> Makes a connection from A to J and C")
        print("------------------------------")
        print("Type Done if the graph is completed")
        print("------------------------------")
        text = input("")
        if head == "":
            
            head = text[0]
            print("SFIUT")
        print("------------------------------")
        if text.lower() == "done":
            break
        elif len(text) < 2:
            print("Wrong Entry")
            print("------------------------------")
        else:
            text = text.upper()
            key = text[0]
            
        
            for i in range(len(text)-1):
                currchar = text[i+1]
                if currchar != key:
                    if key in graph:
                        print(graph[key])
                        graph[key].append(currchar)
                    else:
                        graph[key] = [currchar]
        
                
    



    return [graph, head]

if __name__ == "__main__":
    graph_maker()