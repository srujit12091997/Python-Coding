def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j]> nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums           
    
print(bubbleSort([15,86,47,7,34,67,0,66,24,67,8]))