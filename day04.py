"""
http://www.adventofcode.com/2016/day/4
"""

ROOMS = open('input/04.txt', 'r').read().splitlines()

# Part 1
def checksum(name):
    name = name.replace('-', '')
    occ = [(l, name.count(l)) for l in set(name)]
    occ.sort(key=lambda t: t[0])
    occ.sort(key=lambda t: t[1], reverse=True)
    return ''.join([t[0] for t in occ[:5]])
    
# Part 2
def decrypt(name, sectorID):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = [(' ' if l == '-' else abc[(abc.index(l) + sectorID) % 26]) for l in name]
    return ''.join(decrypted)

room_sum = 0
for room in ROOMS:
    name = room[:-10]
    if checksum(name) == room[-6:-1]:
        sectorID = int(room[-10:-7])
        room_sum += sectorID
        if 'northpole' in decrypt(name, sectorID):
            print('Part 2:', sectorID)

print('Part 1:', room_sum)