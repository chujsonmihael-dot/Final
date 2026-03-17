import binary_search
import DFS
import n_queens
import array_funcs
import utils

tools = {1:"Binary Search",
         2:"Depth First Search",
         3:"N Queens",
         4:"Sorter"}

if __name__ == "__main__":
    print("--Welcome to Multi-Tool v0.1--")
    print("------------------------------")
    print("What tool do you want to use?")
    for key in tools:
        print(f"Type {key} for {tools[key]}")
    print("------------------------------")
    decision = input("")
    print("------------------------------")
    if decision == "1":
        binary_search.binary_search()
    elif decision == "2":
        args = utils.graph_maker()
        DFS.DFS(args[0], args[1])
    elif decision == "3":
        n_queens.main()
    elif decision == "4":
        
        print(f"Sorted Array: {array_funcs.sort(array_funcs.enter_array())}")
        print("------------------------------")
    else:
        print("Error!")
    