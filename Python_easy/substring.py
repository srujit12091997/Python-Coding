def subString(s, t):
    l, r = 0, 0
    while l < len(s) and r < len(t):
        if s[l] == t[r]:
            l +=1
        r +=1
    return l == len(s)
print(subString(s = "abceaeghf", t = "ahbgdce"))