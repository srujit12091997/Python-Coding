def arrLargest(nums):
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    print(largest)
print(arrLargest([1,2,3,4,5]))