from complementary import array_funcs
import time
def binary_search(arr, target):
    arr = array_funcs.sort(arr)
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1

def binary_search_text():
    print("Binary Search")
    print("------------------------------")
    arr = array_funcs.enter_array()
    target = int(input("Type the target value: "))
    print("------------------------------")
    startTime = time.time()
    binary_search(arr, target)
    print(f"Sorted Array is {arr}")
    print(f"The target does not show up in arr!")
    print("------------------------------")
    print(f"The calculations took {time.time()-startTime}")
    print("------------------------------")
    return -1

def binary_search_gui(widgets, array):
    widgets["IntegerEntry"].place(relx=0.5, rely=0.3, anchor="center")
    widgets["IntegerEntryText"].place(relx=0.5, rely=0.2, anchor="center")
    widgets["IntegerEntry"].bind("<Return>", lambda event:  on_enter(widgets, array,  binary_search))
    widgets["SortedArray"].config(text=f"Current Array: {sorted(array)}")
    widgets["SortedArray"].place(relx=0.5, rely=0.1, anchor="center")

def on_enter(widgets, array, callback):
    print("Pressed Enter")
    widgets["IntegerEntry"].place_forget()
    widgets["IntegerEntryText"].place_forget()
    widgets["BinarySearchResult"].config(text=f"Answer is: {callback(array, int(widgets['IntegerEntry'].get()))}")
    widgets["BinarySearchResult"].place(relx=0.5, rely=0.4, anchor="center")

