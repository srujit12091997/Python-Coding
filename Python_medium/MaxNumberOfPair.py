def maxOperations(nums,k):
    nums.sort()
    l,r = 0, len(nums)-1
    operations =0
    while l<r:
        if nums[l]+nums[r] == k:
            operations +=1
            l +=1
            r -=1
        elif nums[l]+nums[r] < k:
            l +=1
        else:
            r -=1
    return operations
print(maxOperations([1,2,3,4], 6))