# remove nearby duplicates.
# sample output:
# heLlo world

def removeNearbyDuplicates(s):
    if len(s) == 1: 
        return s
    elif s[0] == s[1]:
        return removeNearbyDuplicates(s[1:])
    return s[0]+ removeNearbyDuplicates(s[1:])

s = "heeLLloo wwwooorrlllld"
print(removeNearbyDuplicates(s))