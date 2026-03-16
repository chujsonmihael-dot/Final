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
