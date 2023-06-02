from typing import List


class NumArray:
    def __init__(self, nums):
        self.cumulative_sum = [0]
        current_sum = 0
        for num in nums:
            current_sum += num
            self.cumulative_sum.append(current_sum)

    def sumRange(self, left, right):
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)