class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return -1
        return -1

