"""
http://www.adventofcode.com/2016/day/2
"""

import re

INPUT = open('input/03.txt', 'r').read()

# Part 1
TRIANGLES = [[int(g) for g in re.search(
    r'\s+(\d+)\s+(\d+)\s+(\d+)', t).group(1, 2, 3)] for t in INPUT.splitlines()]


def is_triangle(triangle: [int, int, int]) -> bool:
    """Returns true if the given side lengths can form a triangle"""
    for first in range(3):
        for second in range(first + 1, 3):
            if triangle[first] + triangle[second] <= triangle[3 - first - second]:
                return False
    return True


COUNT = sum(int(is_triangle(t)) for t in TRIANGLES)

print('Part 1:', COUNT)

# Part 2
TRIANGLES_VERTICAL = []

for c in range(3):
    for i in range(0, len(TRIANGLES), 3):
        TRIANGLES_VERTICAL.append(
            [TRIANGLES[i][c], TRIANGLES[i + 1][c], TRIANGLES[i + 2][c]])

COUNT = sum(int(is_triangle(t)) for t in TRIANGLES_VERTICAL)

print('Part 2:', COUNT)