from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(next_greater[num])

        return ans