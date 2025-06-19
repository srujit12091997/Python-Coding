def isPerfectSquare(nums):
    left, right = 1, nums
    while left <= right:
        mid = (left+ right)//2
        if mid* mid == nums:
            return True
        if mid * mid < nums:
            left = mid +1
        elif mid * mid > nums:
            right = mid -1
            
        else:
            return True
    return False

print(isPerfectSquare(16))