"""
http://www.adventofcode.com/2016/day/7
"""

import re

addresses = open('input/07.txt', 'r').read().splitlines()

def supportsTLS(address):
    checkOutsideBrackets = matchesABBA(outsideBrackets(address))
    checkInsideBrackets = not matchesABBA(insideBrackets(address))
    return checkOutsideBrackets and checkInsideBrackets

def matchesABBA(string):
    return re.search(r'(\w)(?!\1)(\w)\2\1', string) != None

def outsideBrackets(string):
    return re.sub(r'(?<=\[)\w*(?=\])', '', string)

def insideBrackets(string):
    return re.sub(r'(?:^|(?<=\]))\w*', '', string)

def supportsSSL(address):
    matches = matchesInABA(outsideBrackets(address))
    for m in matches:
        reverse = m[1] + m[0] + m[1]
        if re.search(reverse, insideBrackets(address)) != None:
            return True
    return False
    
def matchesInABA(string):
    matches = []
    while True:
        match = re.search(r'(\w)(?!\1)(\w)\1', string)
        if match == None:
            return matches
        matches.append(match[0])
        string = string[match.start()+1:]
    

print('Part 1:', sum([int(supportsTLS(a)) for a in addresses]))
print('Part 2:', sum([int(supportsSSL(a)) for a in addresses]))