"""
http://www.adventofcode.com/2016/day/2
"""

import re

INPUT = open('input/03.txt', 'r').read()

# Part 1
TRIANGLES = [[int(g) for g in re.search(
    r'\s+(\d+)\s+(\d+)\s+(\d+)', t).group(1, 2, 3)] for t in INPUT.splitlines()]


def isTriangle(triangle):
    for a in range(3):
        for b in range(a + 1, 3):
            if triangle[a] + triangle[b] <= triangle[3 - a - b]:
                return False
    return True


count = sum(int(isTriangle(t)) for t in TRIANGLES)

print('Part 1:', count)

# Part 2
TRIANGLES_VERTICAL = []

for c in range(3):
    for i in range(0, len(TRIANGLES), 3):
        TRIANGLES_VERTICAL.append(
            [TRIANGLES[i][c], TRIANGLES[i + 1][c], TRIANGLES[i + 2][c]])

count = sum(int(isTriangle(t)) for t in TRIANGLES_VERTICAL)

print('Part 2:', count)
