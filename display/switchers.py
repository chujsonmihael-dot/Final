import tkinter as tk
from display.display import ClearDisplay
from display.display import tools

def init(widgets):
    globals().update(widgets)

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
    ClearDisplay(display)
    BackToMenuButton.place(relx=0.5, rely=0.9, anchor="center")

def SwitchToDFS(display):
    ClearDisplay(display)
    BackToMenuButton.place(relx=0.5, rely=0.9, anchor="center")

def SwitchToNQueens(display):
    ClearDisplay(display)    
    BackToMenuButton.place(relx=0.5, rely=0.9, anchor="center")

def SwitchToSorter(display):
    ClearDisplay(display)
    BackToMenuButton.place(relx=0.5, rely=0.9, anchor="center")

def SwitchToFibonacciNumber(display):
    ClearDisplay(display)
    BackToMenuButton.place(relx=0.5, rely=0.9, anchor="center")

def SwitchToEncrypter(display):
    ClearDisplay(display)
    BackToMenuButton.place(relx=0.5, rely=0.9, anchor="center")


keyToFunction = {
    1:SwitchToBinarySearch,
    2:SwitchToDFS,
    3:SwitchToNQueens,
    4:SwitchToSorter,
    5:SwitchToFibonacciNumber,
    6:SwitchToEncrypter
}



    