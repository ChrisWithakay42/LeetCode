from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_array = sorted(arr)
        diff = sorted_array[1] - sorted_array[0]
        for i in range(1, len(arr) - 1):
            if sorted_array[i + 1] - sorted_array[i] != diff:
                return False
        return True