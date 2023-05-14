class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([bit for bit in bin(n)[2:] if bit is '1'])