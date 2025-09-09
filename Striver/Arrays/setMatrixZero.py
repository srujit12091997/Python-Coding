'''def setMatrix(nums):
    nums = [0]* len(nums)
    return nums
print(setMatrix([1,0,1]))

def setMatrix(nums):
    for i in range(len(nums)):
        nums[i] = 0
    return nums
print(setMatrix(([1,0,1])))


def setMatrix(nums):
    nums = [0 for _ in nums]
    return nums
print(setMatrix([1,0,1,]))'''

def setZeros(matrix):
    rows, columns = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                for k in range(rows):
                    if matrix[i][k] != 0:
                        matrix[i][k] =-1
                for k in range(rows):
                    if matrix[k][j] !=0:
                        matrix[k][j] =-1
                for k in range(columns):
                    if matrix[j][i] !=0:
                        matrix[j][i] =-1
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] ==-1:
                matrix[i][j] =0
    return matrix
print(setZeros([[1, 1, 1],[1, 0, 1],[1,1,1]]))