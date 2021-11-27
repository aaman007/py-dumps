"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""

from functools import cache
from typing import List


class Solution:
    """
    This solution is to find possible ways, we can modify it to get the path
    And break as soon as, we reach (m-1), (n-1) cell. We could add the cells
    visited in a path list in order
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def rec(x, y):
            if obstacleGrid[x][y] == 1:
                return 0
            if x == m - 1 and y == n - 1:
                return 1

            ret = 0
            if x + 1 < m:
                ret += rec(x + 1, y)
            if y + 1 < n:
                ret += rec(x, y + 1)

            return ret

        return rec(0, 0)
