def arrangeCoins(num):
    left, right = 1 ,num
    res = 0
    while left<=right:
        coins = mid = (mid/2)* (mid + 1)
        if coins > num:
            right = mid -1
        else:
            left = mid + 1
            res = max(mid, res)
        return res
    
print(arrangeCoins(5))