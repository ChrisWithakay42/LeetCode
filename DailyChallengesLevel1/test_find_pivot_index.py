from find_pivot_index import Solution

def test_find_pivot_index():
    solution = Solution()
    nums = [1,7,3,6,5,6]
    assert solution.pivotIndex(nums) == 3
