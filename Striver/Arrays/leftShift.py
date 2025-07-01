def arrLeftShift(nums):
    if not nums:
        return nums
    first = nums[0]
    nums.pop(0)
    nums.append(first)
    return nums
print(arrLeftShift([1,2,3,4,5]))