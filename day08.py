"""
http://www.adventofcode.com/2016/day/8
"""

import re
import numpy as np

instructions = open('input/08.txt', 'r').read().splitlines()

# initialize screen
screen = [[0 for y in range(6)] for x in range(50)]

# execute instructions
for i in instructions:
    m = re.search(r'(\d+)[^\d]*(\d+)$', i)
    if re.search('rect', i):
        for x in range(int(m[1])):
            for y in range(int(m[2])):
                screen[x][y] = 1
    elif re.search('row', i):
        y = int(m[1])
        s = int(m[2])
        for j in range(s):
            temp = screen[-1][y]
            for x in range(len(screen)-1,-1,-1):
                screen[x][y] = screen[x-1][y]
            screen[0][y] = temp
    else:
        x = int(m[1])
        s = int(m[2])
        for j in range(s):
            temp = screen[x][-1]
            for y in range(len(screen[x])-1,-1,-1):
                screen[x][y] = screen[x][y-1]
            screen[x][0] = temp

print('Part 1:', sum([sum(screen[i]) for i in range(len(screen))]))
print('Part 2:') # Print and read solution from screen
for col in range(len(screen[0])):
    for row in range(len(screen)):
        print(' ' if screen[row][col] == 0 else '#', end='')
    print('')
