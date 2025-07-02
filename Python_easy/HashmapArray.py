#sol1
def findDifference(nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        ans0 = list(set1-set2)
        ans1 = list (set2-set1)
        result = [ans0, ans1]
        return result
    
#sol2    
def arr(nums1,nums2):
    ans0= [] 
    ans1= []
    for num in nums1:
        if num not in nums2 and num not in ans0:
            ans0.append(num)
    for num in nums2:
        if num not in nums1 and num not in ans1:
            ans1.append(num)
    
    result = [ans0, ans1]
    return result