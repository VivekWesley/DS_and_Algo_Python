# Binary search using recursion

def binary_search_helper(arr, value, L, R):
    mid = L + (( R - L ) // 2)
    if L > R:
        return "Not Found"
    if arr[mid] == value:
        return mid
    elif value < arr[mid]:
        return binary_search_helper(arr, value, L, mid-1)
    else:
        return binary_search_helper(arr, value, mid+1, R)
    

arr = [ 0, 2, 8, 88, 90, 999, 1111 ]
value = 88

def binary_search(arr, value ):
    
    return binary_search_helper(arr, value, 0, len(arr)-1)

print(binary_search(arr, value))