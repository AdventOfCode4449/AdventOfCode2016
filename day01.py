"""
http://www.adventofcode.com/2016/day/1
"""

import numpy

FILE = open('input/01.txt', 'r')
ROUTE = FILE.read().split(', ')

# Part 1
POS = [0, 0]
DIR = [0, 1]
PLACES_VISITED = [[0,0]]

for step in ROUTE:
    if step[0] == 'R':
        DIR = list(numpy.dot(DIR, [[0, 1], [-1, 0]]))
    else:
        DIR = list(numpy.dot(DIR, [[0, -1], [1, 0]]))
    for i in range(int(step[1:])):
        POS[0] += DIR[0]
        POS[1] += DIR[1]
        PLACES_VISITED.append(POS[:])

print('Part 1:', abs(POS[0]) + abs(POS[1]))

# Part 2
for index, place in enumerate(PLACES_VISITED):
    if place in PLACES_VISITED[:index]:
        print('Part 2:', abs(place[0]) + abs(place[1]))
        break
