def linear_search(arr, target):
    # Your code here
    for e in range(len(arr)):
        if arr[e] == target:
            return e
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle_index = (left + right) // 2

        if target == arr[middle_index]:
            return middle_index
        elif arr[middle_index] > target:
            # cut right side
            right = middle_index - 1
        elif arr[middle_index] < target:
            # cut left side
            left = middle_index + 1

    return -1  # not found
