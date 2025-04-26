# O(1) time operation
def insertEnd(arr, n, length, capacity):
    # check if length is less than capacity
    if length < capacity:
        # if yes, then proceed with the insertion
        # increment the size of the array
        arr[length] = n

# O(1) time operation
def removeEnd(arr, length):
    # check if length is greater than zero
    if length > 0:
        # Overwrite the value, setting it to 0 or null
        # decrement the size of the array
        arr[length - 1] = 0
    
# O(n) time operation
def insertMiddle(arr, i, n, length):
    # Move the elements from length - 1 to i by - 1 position to the right
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    # insert the element at ith position
    # increment the size of the array as well
    arr[i] = n

# O(n) time operation
def removeMiddle(arr, i, length):
    # Move the elements from pos i + 1 to last by - 1 position to the left
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # Optionally overwrite the last element with value 0 or -1 to indicate empty index
    # decrement the size of the array as well
    arr[length - 1] = 0

# O(n) time operation
def print(arr, capacity):
    # traverse through the array and print the elements
    for i in range(capacity):
        print(arr[i])
