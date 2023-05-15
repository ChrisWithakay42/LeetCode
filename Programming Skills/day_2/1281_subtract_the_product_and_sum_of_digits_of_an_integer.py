from functools import reduce
from operator import mul


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(abs(n))]
        prod, su = 1, 0
        for d in digits:
            prod *= d
            su += d
        return prod - su
        # The below functional approach has a time complexity
        # return reduce(mul, digits) - sum(digits)
