class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_word = words[::-1]
        result = " ".join(reverse_word)
        return result