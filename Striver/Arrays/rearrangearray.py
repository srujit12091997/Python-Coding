def rearrangearray(nums):
    arr1 = []
    arr2 = []
    final_array = [None] * len(nums)
    for i in range(len(nums)):
        if nums[i]>0:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])            
        for j in range(len(arr1)):
            final_array[2*j] = arr1[j]
        for k in range(len(arr2)):
            final_array[2*k+1] = arr2[k]    
    return final_array
print(rearrangearray([1,2,-4,-5]))