class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 != 0 or high % 2 != 0)
        # the second solution times out as it is O(n)
        # return len([num for num in range(low, high + 1) if num % 2 != 0])