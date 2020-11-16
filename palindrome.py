# palindrome or not

# sample output:
# palindrome string

def palindrome(str):
    rev_String = ''

    for i in reversed(range(len(str))):
        rev_String += str[i]
    if (str == ''.join(rev_String)):
        print ("palindrome string")
    else:
        print ("not a palindrome string")

str = "ada"
palindrome(str)