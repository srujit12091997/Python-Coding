def sortArr(nums):
    even = []
    odd = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    return even+odd
print(sortArr([1,56,98,65,34,56]))