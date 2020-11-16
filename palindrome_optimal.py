# palindrime or not optimal in terms  of space because of the use of the array instead of string

# sample output: 
# palindrome string

def palindrome(str):
    rev = []

    for i in reversed(range(len(str))):
        rev.append(str[i])

    if (''.join(rev) == str):
        return "palindrome string"
    return "not a palindrome string"

str = "dad"
print(palindrome(str))