# find nth fibonacci number using recursion.

#  sample output:
# 21

def findnthfibnumber(n, map={1: 0, 2: 1}):
    if n in map:
        return map[n]
    else:
        map[n] = findnthfibnumber(n-1, map) + findnthfibnumber(n-2, map)
        return map[n]

print (findnthfibnumber(9))

