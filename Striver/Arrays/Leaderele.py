'''def printLeader(nums):
    leader = []
    for i in range(len(nums)):
        is_Leader = True
        for j in range(i+1,len(nums)):
            if nums[i]<=nums[j]:
                is_Leader = False
                break
        if is_Leader:
            leader.append(nums[i])
    return leader
print(printLeader([10,22,12,3,0,6]))'''


def findLeader(nums):
    leader = []
    r = float('-inf')
    for l in range(len(nums)-1,-1,-1):
        if nums[l] > r:
            leader.append(nums[l])
            r = nums[l]
    return leader[::-1]
print(findLeader([10,22,12,3,0,6]))