# smallest common element present in all the arrays.

# sample output: 
# 4

def find_smallest_common_element_by_comparison(arr1, arr2, arr3):
    if len(arr1) < 1 or len(arr2) < 1 or len(arr3) < 1:
        return "length issue."
    p1 = 0
    p2 = 0
    p3 = 0

    while p1 <= len(arr1) - 1 and p2 <= len(arr2) - 1 and p3 <= len(arr3) - 1:
        
        if arr1[p1] == arr2[p2] == arr3[p3]:
            return arr1[p1]

        if arr1[p1] <= arr2[p2] and arr1[p1] <= arr3[p3]:
            p1 += 1
        elif arr2[p2] <= arr1[p1] and arr2[p2] <= arr3[p3]:
            p2 += 1
        elif arr3[p3] <= arr1[p1] and arr3[p3] <= arr2[p2]:
            p3 += 1
    return "Not found"

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [2, 4, 6, 8, 10]
arr3 = [4, 8, 16, 32, 64]

print (find_smallest_common_element_by_comparison(arr1, arr2, arr3))