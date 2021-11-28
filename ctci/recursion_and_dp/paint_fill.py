"""
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""
from typing import List


class Solution:
    def fill(self, image, sr, sc, oldColor, newColor):
        image[sr][sc] = newColor
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in steps:
            nr, nc = sr + dx, sc + dy
            if nr < 0 or nc < 0 or nr >= len(image) or nc >= len(image[0]) or image[nr][nc] != oldColor:
                continue
            self.fill(image, nr, nc, oldColor, newColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image

        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image


