"""
http://www.adventofcode.com/2016/day/5
"""

import hashlib

DOOR_ID = open('input/05.txt', 'r').read()

def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def pw1(id):
    i = 0
    pw = ''
    while len(pw) < 8:
        h = md5(id + str(i))
        if h[:5] == '00000':
            pw += h[5]
        i+=1
    return pw

def pw2(id):
    pw = {}
    i = 0
    while len(pw.keys()) < 8:
        h = md5(id + str(i))
        if h[:5] == '00000' and h[5].isdigit():
            pos = int(h[5])
            val = h[6]
            if pos < 8 and (not pos in pw):
                pw[pos] = val
        i += 1
    return ''.join([pw[i] for i in range(8)])


print('Part 1:', pw1(DOOR_ID))
print('Part 2:', pw2(DOOR_ID))
