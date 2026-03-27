import tkinter as tk

tools = tools = {1:"Binary Search",
         2:"Depth First Search",
         3:"N Queens",
         4:"Sorter",
         5:"Fibonacci Number",
         6:"Encrypter"}

State = "mainmenu"
def MultiToolMainWindow():
    
    import display.switchers as switchers
    display = tk.Tk()
    display.title("Multi-Tool v0.1")
    display.geometry("640x360") # SIZE
    display.configure(bg="#3d3d3d")
    switchers.init(DefineWidgets(display))
    switchers.SwitchToMainMenu(display)
    display.mainloop()

def ClearDisplay(display):
    for widget in display.winfo_children():
        widget.place_forget()

def DefineWidgets(display):
    import display.switchers as switchers
    Widgets = {}
    Widgets["BackToMenuButton"] = tk.Button(display, text="Back to Menu", font=("Sans-Serif", 14), command=lambda: switchers.SwitchToMainMenu(display))
    return Widgets







    



if __name__ == "__main__":
    
    MultiToolMainWindow()