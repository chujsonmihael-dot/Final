import sort
import time
def binary_search():
    print("Binary Search")
    print("------------------------------")
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
    target = int(input("Type the target value: "))
    print("------------------------------")
    startTime = time.time()
    arr = sort.sort(arr)
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            print(f"Sorted Array is {arr}")
            print(f"Answer is {mid}")
            print("------------------------------")
            print(f"The calculations took {time.time()-startTime}")
            print("------------------------------")
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    print(f"Sorted Array is {arr}")
    print(f"The target does not show up in arr!")
    print("------------------------------")
    print(f"The calculations took {time.time()-startTime}")
    print("------------------------------")
    return -1