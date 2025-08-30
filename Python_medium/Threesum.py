def threeSum(nums):
    nums.sort()
    result =[]
    for i in range(len(nums)-1):
        if i > 0 and nums[i] ==nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        target = -nums[i]
        while l < r:
            current_sum = nums[l]+ nums[r]
            if current_sum == target:
                result.append([(nums[i],nums[l],nums[r])])
                while l <r and nums[l] ==nums[l+1]:
                    l +=1
                while l < r and nums[r] == nums[r-1]:
                    r -=1
                l+=1
                r-=1
            elif current_sum < target:
                l +=1
            else:
                r -=1
    return result
print(threeSum([-1,0,1,2,-1,-4]))

        
         