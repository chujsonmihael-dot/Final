import binary_search
import DFS
import n_queens
import sort

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
        DFS.DFS()
    elif decision == "3":
        n_queens.n_queens()
    elif decision == "4":
        sort.sort()
    else:
        print("Error!")
    