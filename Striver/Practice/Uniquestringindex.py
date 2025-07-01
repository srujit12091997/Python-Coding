'''Description:
Given a string s, find the index of the first non-repeating character. If there is no unique character, return -1.'''


def uniqueStr(s):
    for i in range(len(s)):
        counter=0
        for j in range(len(s)):
            if s[i] == s[j]:
                counter +=1
        if counter ==1:
            return i
    return -1                      
print(uniqueStr("loveleetcode"))