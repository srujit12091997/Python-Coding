def drawTriangle(n):
    for i in range(0, n):
        for j in range(i+1):
            print("*", end="")
        print()
    pass
drawTriangle(5)