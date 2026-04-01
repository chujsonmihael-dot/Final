import tkinter as tk
from display.display import ClearDisplay
from display.display import tools
from complementary import array_funcs, utils

import programs.binary_search as binary_search
import programs.DFS as DFS

# module-level storage for widgets instead of injecting into globals()
_widgets = None

def init(widgets):
    global _widgets
    _widgets = widgets

def SwitchToMainMenu(display):
    global MainTitle1, MainTitle2

    ClearDisplay(display)
    MainTitle1 = tk.Label(display, text="Welcome to", font=("Arial", 24, "bold"), bg="#3d3d3d",fg="#d4d4d4")
    MainTitle2 = tk.Label(display, text="Multi-Tool v0.1", font=("Arial", 32, "bold"), bg="#3d3d3d",fg="#d4d4d4")

    MainTitle1.place(relx=0.5,rely=0.05,anchor="center")
    MainTitle2.place(relx=0.5, rely=0.175, anchor="center")

    def ButtonClick(key):
        global State
        State = tools[key]
        print(State)
        keyToFunction[key](display)
    
    posy = 0.3
    posx = 0.025
    buttons = []
    for key in tools:
        NewButton = tk.Button(display, text=tools[key], font=("Sans-Serif", 14), command=lambda k = key: ButtonClick(k))
        NewButton.place(anchor="w", relx=posx,rely=posy )
        buttons.append(NewButton)
        posy+=0.125



def SwitchToBinarySearch(display):
    def on_array_enter(array):
        ClearDisplay(display)
        _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")
        binary_search.binary_search_gui(_widgets, array)

    ClearDisplay(display)
    _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")

    array_funcs.enter_array_gui(_widgets, on_array_enter)
    

def SwitchToDFS(display):
    ClearDisplay(display)
    def on_enter(result):
        _widgets["DFSResultText"].place(relx=0.5, rely=0.4, anchor="center")
        _widgets["DFSResult"].place(relx=0.5, rely=0.5, anchor="center")
        _widgets["DFSResult"].config(text=f"{result}")
        _widgets["DFSGraphEntry"].place_forget()
        
    _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")
    utils.graph_maker_gui(_widgets, lambda graph, head: DFS.DFS_gui(graph, head, on_enter))
    

def SwitchToNQueens(display):
    ClearDisplay(display)
    _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")

def SwitchToSorter(display):
    ClearDisplay(display)
    _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")

def SwitchToFibonacciNumber(display):
    ClearDisplay(display)
    _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")

def SwitchToEncrypter(display):
    ClearDisplay(display)
    _widgets["BackToMenuButton"].place(relx=0.5, rely=0.9, anchor="center")


keyToFunction = {
    1:SwitchToBinarySearch,
    2:SwitchToDFS,
    3:SwitchToNQueens,
    4:SwitchToSorter,
    5:SwitchToFibonacciNumber,
    6:SwitchToEncrypter
}



    