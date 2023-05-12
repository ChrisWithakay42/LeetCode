class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        new_sentence = ' '.join(reversed_words)
        return new_sentence
