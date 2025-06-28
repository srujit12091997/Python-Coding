def maxVowels(s,k):
    n = len(s)
    vowels ={'a','e','i','o','u'}
    count = 0
    
    for i in range(k):
        if s[i] in vowels:
            count +=1
    max_vowels = count
    
    for i in range(k, n):
        if s[i] in vowels:
            count +=1
        if s[i-k] in vowels:
            count -=1
        max_vowels = max(count, max_vowels)
    return max_vowels
print(maxVowels(s = "abciiidef", k = 3))