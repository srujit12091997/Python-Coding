def quicksort(nums):
    if len(nums)<=1:
        return nums
    pivot = nums[len(nums)//2]
    left= [x for x in nums if x < pivot]
    middle=[x for x in nums if x == pivot]
    right =[x for x in nums if x > pivot]
    return quicksort(left) + quicksort(middle) + quicksort(right)    
print(quicksort([7,8,9,12,15,34,56]))
