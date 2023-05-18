from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        dict_s = defaultdict(int)
        for val in dict_s:
            dict_s[val] += 1

        dict_t = defaultdict(int)
        for val in dict_t:
            dict_t[val] += 1

        return dict_s == dict_t
