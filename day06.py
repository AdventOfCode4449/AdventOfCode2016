"""
http://www.adventofcode.com/2016/day/6
"""

rows = open('input/06.txt', 'r').read().splitlines()
cols = [[rows[i][j] for i in range(len(rows))] for j in range(len(rows[0]))]

message1 = ''
message2 = ''
for i in range(len(cols)):
    count = {}
    for c in range(len(cols[i])):
        if cols[i][c] in count:
            count[cols[i][c]] += 1
        else:
            count[cols[i][c]] = 0
    message1 += list(count)[list(count.values()).index(max(count.values()))]
    message2 += list(count)[list(count.values()).index(min(count.values()))]

print('Part 1:', message1)
print('Part 2:', message2)