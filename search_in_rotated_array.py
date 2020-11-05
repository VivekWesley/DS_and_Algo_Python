# search element in rotated array using recursion.

# SAMPLE OUTPUT: 
# 6

def search_in_rotated_array_helper(arr, L, R, target):
    if L > R :
        return "Not Found"
    mid = L + (R-L)//2
    if arr[mid] == target:
        return mid
    if arr[L] <= arr[mid] and target <= arr[mid] and target >= arr[L]:
        return search_in_rotated_array_helper(arr, L, mid-1, target)
    elif arr[mid] <= arr[R] and target >= arr[mid] and target <= arr[R]:
        return search_in_rotated_array_helper(arr, mid+1, R, target)
    
    elif arr[R] > arr[mid]:
        return search_in_rotated_array_helper(arr, L, mid-1, target)
    return search_in_rotated_array_helper(arr, mid+1, R, target) 

arr = [ 6, 8, 10, 12, 16, 1, 2, 3, 4, 5 ]
target = 2

def search_in_rotated_array(arr, target):
    return search_in_rotated_array_helper(arr, 0, len(arr)-1, target)

print(search_in_rotated_array(arr, target))