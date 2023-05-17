from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        initial_slope = (y1 - y0) / (x1 - x0) if (x1 - x0) != 0 else float('inf')

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            slope = (yi - y0) / (xi - x0) if (xi - x0) != 0 else float('inf')
            if slope != initial_slope:
                return False

        return True
