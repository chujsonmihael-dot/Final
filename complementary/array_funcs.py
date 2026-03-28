def sort(arr):
    return sorted(arr)

def enter_array():
    print("Enter the array")
    arr = []
    while True:
        print(f"Current array is {arr}")
        print("Type the next value")
        print("Type Done to end the array")
        print("------------------------------")
        val = input("")
        if val == "Done":
            break
        elif val.isdigit():
            arr.append(int(val))
    print("------------------------------")
    return arr

def enter_array_gui(widgets, callback):
    widgets["ArrayEntry"].place(relx=0.5, rely=0.3, anchor="center")
    widgets["ArrayEntryText"].place(relx=0.5, rely=0.2, anchor="center")

    def on_enter(widgets):
        print("Pressed Enter")
        widgets["ArrayEntry"].place_forget()
        
        callback(list(map(int, widgets["ArrayEntry"].get().split(","))))
    widgets["ArrayEntry"].bind("<Return>", lambda event:  on_enter(widgets))

    print("klikło xd")