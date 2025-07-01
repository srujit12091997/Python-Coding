def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i-1
        keys = nums[i]
        while j >= 0 and nums[j]> keys:
            nums[j+1] = nums[j]
            j -=1
            nums[j+1] = keys
    return nums
print(insertionSort([14,9,15,12,6,4,66,999,35,6]))