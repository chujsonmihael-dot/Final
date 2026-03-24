import tkinter as tk
import main

tools = main.tools


def MultiToolMainWindow():
    display = tk.Tk()
    display.title("Multi-Tool v0.1")
    display.geometry("640x360") # SIZE
    display.configure(bg="#3d3d3d")

    MainTitle1 = tk.Label(display, text="Welcome to", font=("Arial", 24, "bold"), bg="#3d3d3d",fg="#d4d4d4")
    MainTitle2 = tk.Label(display, text="Multi-Tool v0.1", font=("Arial", 32, "bold"), bg="#3d3d3d",fg="#d4d4d4")

    MainTitle1.place(relx=0.5,rely=0.05,anchor="center")
    MainTitle2.place(relx=0.5, rely=0.175, anchor="center")

    def ButtonClick(key):
        print(tools[key])

    #ADDNS BUTTONS
    posy = 0.3
    posx = 0.025
    buttons = []
    for key in tools:
        NewButton = tk.Button(display, text=tools[key], font=("Sans-Serif", 14), command=lambda k = key: ButtonClick(k))
        NewButton.place(anchor="w", relx=posx,rely=posy )
        buttons.append(NewButton)
        posy+=0.125

    display.mainloop()

if __name__ == "__main__":
    MultiToolMainWindow()