"""
http://www.adventofcode.com/2016/day/9
"""

import re

input = open('input/09.txt', 'r').read()
input = re.sub(r'\r?\n', '', input)
input = re.sub(r'\s+', '', input)


def decodeLength1(string):
    length = len(string)
    index = 0
    while(True):
        match = re.search(r'\((\d+)x(\d+)\)', string[index:])
        if match:
            charcount = int(match.groups()[0])
            multiplier = int(match.groups()[1])
            length += charcount * (multiplier - 1) - len(match.group())
            index += match.end() + charcount
        else:
            break
    return length


def decodedLength2(string):
    length = len(string)
    index = 0
    while True:
        match = re.search(r'\((\d+)x(\d+)\)', string[index:])
        if match:
            charcount = int(match.groups()[0])
            multiplier = int(match.groups()[1])
            length += decodedLength2(string[index+match.end():index+match.end() + charcount]) * multiplier - len(match.group()) - charcount
            index += match.end() + charcount
        else:
            return length


# print('Part 1:', decompressionlength1(input))
print('Part 2:', decodedLength2(input))