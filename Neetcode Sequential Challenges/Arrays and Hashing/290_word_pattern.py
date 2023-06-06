class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        pattern_dict = {}
        for i, c in enumerate(pattern):
            word = words[i]
            if c in pattern_dict:
                if pattern_dict[c] != word:
                    return False
            else:
                if word in pattern_dict.values():
                    return False
                pattern_dict[c] = word

        return True
