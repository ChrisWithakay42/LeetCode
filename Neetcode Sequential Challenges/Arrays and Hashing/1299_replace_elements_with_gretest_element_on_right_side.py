from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_element = arr[n-1]
        arr[n-1] = -1

        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = max_element
            max_element = max(max_element, temp)

        return arr
