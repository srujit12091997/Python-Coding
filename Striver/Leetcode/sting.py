def Maxdif(s):
    a1 = 0 
    a2 = 0 
    freq ={}
    for char in s:
        if char not in freq:
            freq[char] = 0
        freq[char] +=1
    for val in freq.values():
        if val %2 ==0:
            a2 += val
        else:
            a1 += val

    diff = a1 - a2
    return diff

        
'''for val in freq.values():
        if val % 2 == 0:
            a2 += val
        else:
            a1 += val
    diff = a1-a2
    return diff
print(Maxdif("aaabbbcccdddddddeeee"))'''