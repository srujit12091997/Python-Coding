def lastOccurance(arr, n, x):
    low, high = 0, n-1
    last = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            last = mid
            low = mid +1
        elif arr[mid] < x:
            low = mid +1
        else:
            high = mid -1
    return last
print(lastOccurance([3,4,13,13,13,20,40], 7, 13))
            