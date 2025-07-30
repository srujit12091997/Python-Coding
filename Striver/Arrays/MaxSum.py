def maxSum(nums):
    curr = nums[0]
    max_sum = curr
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            curr +=nums[i]
        else:
            curr = nums[i]
        max_sum = max(curr,max_sum)
    return max_sum
print(maxSum([1,2,3,4,2,3,5,6,8,9]))