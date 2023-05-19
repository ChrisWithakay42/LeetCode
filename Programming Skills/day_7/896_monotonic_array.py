from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        increasing = decreasing = True

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False

        return increasing or decreasing