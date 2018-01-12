"""
http://www.adventofcode.com/2016/day/2
"""

COMMANDS = open('input/02.txt', 'r').read().splitlines()
DIR = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
COMBINATION = []

# Part 1
NUMPAD = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

r = 1
c = 1

for line in COMMANDS:
    for char in line:
        r = min([max([r + DIR[char][0], 0]), 2])
        c = min([max([c + DIR[char][1], 0]), 2])
    COMBINATION.append(NUMPAD[r][c])

print('Part 1:', ''.join(str(i) for i in COMBINATION))

# Part 2
STRANGE_NUMPAD = (
    (None, None, '1', None, None),
    (None, '2', '3', '4', None),
    ('5', '6', '7', '8', '9'),
    (None, 'A', 'B', 'C', None),
    (None, None, 'D', None, None)
)

COMBINATION.clear()
r = 2
c = 0
MAX = (2, 3, 4, 3, 2)
MIN = (2, 1, 0, 1, 2)

for line in COMMANDS:
    for char in line:
        r = min([max([r + DIR[char][0], MIN[c]]), MAX[c]])
        c = min([max([c + DIR[char][1], MIN[r]]), MAX[r]])
    COMBINATION.append(STRANGE_NUMPAD[r][c])

print('Part 2:', ''.join(COMBINATION))
