class Solution:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:

        result = 0

        for i in range(len(s)):
            current_value = self.values[s[i]]

            if i > 0 and current_value > self.values[s[i - 1]]:
                result += current_value - 2 * self.values[s[i - 1]]
            else:
                result += current_value

        return result
