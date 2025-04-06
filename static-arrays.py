# In languages like Java, C++ and C#, arrays have to have an allocated size and type when initialized. 
# Static arrays are fixed in size, means the size is fixed once the array is declared.
# In other languages like Python and JS, arrays are dynamic in size as their capacity grows 
# dynamically as we insert the element - they are not fixed in size

# Insert n at the end of array
# Length is the number of elements in the array
# Capacity is the size (aka memory allocated for array to store elements)
# O(1) time operation
def insertEnd(arr, n, length, capacity):
    # check if length is less than capacity
    # if yes - then we can only store the element in the array
    if length < capacity:
        arr[length] = n

    # increment the length by 1
    length = length + 1

# Remove the last element from the array 
# Overwrite with some value such as 0 or -1
# Decrement the length as well by 1
# O(1) time operation
def removeEnd(arr, length):
    # check if the array is not empty
    if length > 0:
        arr[length - 1] = 0

    # decrement the length by 1
    length = length - 1

# Insert the element in the middle of array
# Shift the elements starting from index i + 1 till end to the right
# In worst case scenario, we would have to shift n number of elements to the right
# O(n) time operation
def insertMiddle(arr, i, n, length):
    # Shift the elemens to the right
    for i in range(length - 1, i - 1, -1):
        arr[i + 1] = arr[i]

    # After shifting the element, insert the element at index i
    arr[i] = n

    # increment the length by 1
    length = length + 1
    
# Remove the element at index i
# Shift the elements starting from index i + 1 to the left 
# In worst case scenario, we would have to shift n number of elements to the left
# O(n) time operation
def removeMiddle(arr, i, length):
    # Shift the elemnts to the left
    for i in range(i + 1, length):
        arr[i - 1] = arr[i]
    
    # decrement the length by 1
    length = length - 1

# Traversing through an array and print the elements
def printArr(arr):
    for i in range(len(arr)):
        print(arr[i])
