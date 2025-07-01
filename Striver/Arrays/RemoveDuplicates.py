def remDup(nums):
    hashset = set()
    
    for num in nums:
        if num not in hashset:
            hashset.add(num)
    return hashset
print(remDup([1,1,2,2,3,3,4,4,5,5]))