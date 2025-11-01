def binarySearch(arr,target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid +1
        else:
            high = mid -1
    return -1
print(binarySearch([3,4,6,7,9,12,16,17], 6))