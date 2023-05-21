class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(' ')[-1])
        lengts = 0
        found_word = False

        for i in range(len(s) -1, -1, -1):
            if s[i] == ' ':
                if found_word:
                    break
            else:
                length += 1
                found_word = True

        return length


