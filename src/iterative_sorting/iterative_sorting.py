# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i --> confusing lol
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                # arr[j] = cur_index -- no.
                # change the smallest index to index j
                smallest_index = j

        # change smallest index's value to i's value &
        # change the value at i to the smallest index's value
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below

# Loop through your array
# Compare each element to its neighbor
# If elements in wrong position (relative to each other, swap them)
# If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.


def bubble_sort(arr):
    # Your code here
    for i in range(len(arr)):
        # smallest_element = i
        print(f'array at index i {i}: {arr[i]}')
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                print(f'array at index j {j}: {arr[j]}')
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f'arr now: {arr}')
    return arr


array1 = [9, 0, 1, 8, 2, 20]
# 1st pass: 0, 9, 1, 8, 2
# 1st pass: 0, 1, 9, 8, 2
# 1st pass:0, 1, 8, 2, 9
bubble_sort(array1)
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
