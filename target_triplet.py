# target triple program:

# sample output: 
# 1 ,  9 ,  10

def target_triplet(arr, target):
    if (len(arr) < 1):
        return "length issue."

    left = arr[1]
    right = len(arr)-1

    for i in range(len(arr) - 2):

        while left < right:
            if arr[i] + arr[left] + arr[right] == target:
                return print (arr[i], ", ", arr[left], ", ", arr[right])
            elif arr[i] + arr[left] + arr[right] < target:
                left += 1
            elif arr[i] + arr[left] + arr[right] > target:
                right -= 1 
        return " NO MATCH" 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 20

target_triplet(arr, target)