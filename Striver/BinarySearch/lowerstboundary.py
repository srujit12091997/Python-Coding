def lowBoundary(arr, n, x):
    low, high = 0, len(arr)-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print(lowBoundary([1,2,2,2,2,2,2,3,4,5,6,7,8,9,10], 15, 5))