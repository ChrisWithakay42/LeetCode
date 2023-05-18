class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''.join([char1 + char2 for char1, char2 in zip(word1, word2)])

        merged += word1[len(word2):]
        merged += word2[len(word1):]

        return merged

