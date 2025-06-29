def longestSubArray(nums):
    l = 0
    max_len = 0
    sub_arr = 0
    for r in range(len(nums)):
        if nums[l] == 0:
            sub_arr +=1
        while sub_arr > 1:
            if nums[l] == 0:
                sub_arr -=1
            l +=1
        max_len = max(max_len, r - l)
    return max_len
print(longestSubArray(nums = [1,1,0,1,1,1,1,0,0]))