# searching an element in a rotated array using bynary search.

def rotated_search_helper(arr, low, high, key):
    if low > high:
        return "No match found"

    mid = low + (high-low) // 2
    
    if arr[mid] == key:
        return mid

    if arr[low] <= arr[mid] and key <= arr[mid] and key >= arr[low]:
        return rotated_search_helper(arr, low, mid-1, key)

    elif arr[high] >= arr[mid] and key >= arr[mid] and key <= arr[high]:
        return rotated_search_helper(arr, mid+1, high, key)
    
    elif arr[mid]>arr[low]:
        return rotated_search_helper(arr, mid+1, high, key)
    
    elif arr[mid]<arr[high]:
        return rotated_search_helper(arr, low, mid-1, key)
    
    return -1

arr = [64, 128, 256, 512, 2, 4, 8, 16, 32]
key = 32

def rotated_search(arr, key):
    return rotated_search_helper(arr, 0, len(arr)-1, key)

print (key,"found at index: ",rotated_search(arr, key))