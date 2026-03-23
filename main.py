from programs import binary_search, DFS, Encrypter, fibonacci_numbers, n_queens

from complementary import utils, array_funcs

import tkinter as tk

tools = {1:"Binary Search",
         2:"Depth First Search",
         3:"N Queens",
         4:"Sorter",
         5:"Fibonacci Number",
         6:"Encrypter"}
def MuliToolMainConsole():
    print("--Welcome to Multi-Tool v0.1--")
    print("------------------------------")
    while True:
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
        elif decision == "5":
            fibonacci_numbers.fib_n()
        elif decision == "6":
            Encrypter.Main()
        else:
            print("Error!")
            print("------------------------------")

def MultiToolMainWindow():
    display = tk.Tk()
    display.title("Multi-Tool v0.1")
    display.geometry("640x360") # SIZE
    display.configure(bg="#3d3d3d")

    MainTitle1 = tk.Label(display, text="Welcome to", font=("Arial", 24, "bold"), bg="#3d3d3d",fg="#d4d4d4")
    MainTitle2 = tk.Label(display, text="Multi-Tool v0.1", font=("Arial", 32, "bold"), bg="#3d3d3d",fg="#d4d4d4")

    MainTitle1.place(relx=0.5,rely=0.05,anchor="center")
    MainTitle2.place(relx=0.5, rely=0.175, anchor="center")


    display.mainloop()

if __name__ == "__main__":
    MultiToolMainWindow()
    
    
    
    
    