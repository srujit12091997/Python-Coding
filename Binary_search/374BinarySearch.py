def guessNumber(n):
    left, right = 1 , n
    while left <= right:
        mid = (left+ right)//2
        res = guess(mid)
        if res< mid:
            right = mid -1
        if res> mid:
            left = mid +1
        else:
            return mid
    return -1
        
print(guessNumber(10))