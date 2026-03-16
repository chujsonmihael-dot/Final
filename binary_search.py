import array_funcs
import time
def binary_search():
    print("Binary Search")
    print("------------------------------")
    arr = array_funcs.enter_array()
    target = int(input("Type the target value: "))
    print("------------------------------")
    startTime = time.time()
    arr = array_funcs.sort(arr)
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