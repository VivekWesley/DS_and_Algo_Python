# move common elements(0) to the left side.

# sample output: 
# oroginal array:  [2, 0, 5, 6, 0, 0, 5, 8]
# Moved array:  [0, 0, 0, 2, 5, 6, 5, 8]

def move_common_element(arr):
    if len(arr) < 1:
        return "Length issues"
    
    R = len(arr) - 1
    W = len(arr) - 1

    while(R>=0):
        if arr[R]!=0:
            arr[W] = arr[R]
            W -= 1
        R -= 1

    while (W>=0):
        arr[W] = 0
        W -= 1
    return arr
   
arr = [ 2, 0, 5, 6, 0, 0, 5, 8]

print("oroginal array: ", arr)
print ("Moved array: ", move_common_element(arr))