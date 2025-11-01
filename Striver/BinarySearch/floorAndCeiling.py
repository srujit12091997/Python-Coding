def floorCeiling(arr, n, x):
    low, high = 0, n-1
    floor_Val, ceil_val = -1, -1 
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == x:
            return arr[mid], arr[mid]
        elif arr[mid] < x:
            floor_val = arr[mid]
            low = mid+1
        else:
            ceil_val = arr[mid]
            high = mid -1
    return floor_val, ceil_val        
print(floorCeiling([3, 4, 4, 7, 8, 10], 6, 5))