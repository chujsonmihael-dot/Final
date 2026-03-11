import xd
def binary_search(arr, target):
    arr = xd.sort(arr)
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(arr, target)
    if result is not None:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")