# decimal to binary conversion

# sample output:
# 1010

def decimalToBinaryConversion(n):
    if n<=1:
        return str(n)
    else: 
        return decimalToBinaryConversion(n//2) + decimalToBinaryConversion(n%2)
n = 10
print(decimalToBinaryConversion(n))