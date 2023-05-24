from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Variable to keep track of the count of elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
