from functools import reduce
from operator import mul


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(abs(n))]
        return reduce(mul, digits) - sum(digits)
