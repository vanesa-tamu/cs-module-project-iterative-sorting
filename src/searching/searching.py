def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if i == target:
            print(f'i: {i}, target: {target}')
            return target

    return -1   # not found


array1 = [9, 0, 1, 8, 2, 20]
print(linear_search(array1, 2))


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    right = len(arr)-1
    left = 0

    while left <= right:
        # find middle
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:  # arr[mid] > target:
            right = mid - 1

    return -1  # not found


array2 = [0, 1, 2, 8, 9, 15, 20]
print(binary_search(array2, 20))
