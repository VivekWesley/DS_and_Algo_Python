# print subset/powerset

# sample output:
# 123
# 12
# 13
# 1
# 23
# 2
# 3

def subset(s, index, holder):
    
    if index == len(s):
        print(holder)
        return
    
    subset(s, index+1, holder + s[index])
    
    subset(s, index+1, holder)

s= "123"
holder=""
index = 0

subset(s, index, holder)