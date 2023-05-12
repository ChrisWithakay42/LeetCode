class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        word = ""

        for char in s:
            if char == " ":
                result += word[::-1] + " "
                word = ""
            else:
                word += char
        result += word[::-1]
        return result