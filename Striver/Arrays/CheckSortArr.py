def arrSort(nums,n):
    l,r = 0 , 1
    while r< len(nums):
        if nums[r]<nums[l]:
            return False
        l += 1
        r += 1
    return True    
        
print(arrSort([1,2,3,4,5,1,3,2,0],11))

def isSorted(nums):
    ascending = True
    descending = True

    for i in range(1, len(nums)):
        if nums[i]< nums[i-1]:
            ascending = False
        if nums[i] > nums[i-1]:
            descending = False
    return ascending or descending
                         
print(isSorted([1,2,3,4,5]))