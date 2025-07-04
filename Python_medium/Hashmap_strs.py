def closeStrings(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    if set1 != set2:
        return False
    freq1 =Counter(word1)
    freq2 = Counter(word2)
    return sorted(freq1.values()) == sorted(freq2.values())