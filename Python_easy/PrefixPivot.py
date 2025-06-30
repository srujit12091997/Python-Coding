def pivotIndex(nums):
    total_sum = 0
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total_sum -left_sum +i:
            return i
        left_sum += nums[i]
    return -1
print(pivotIndex(nums = [2,1,-1]))