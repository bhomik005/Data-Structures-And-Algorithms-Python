class DynamicArray:

    # constructor implementation    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = 0
        self.capacity = capacity

    # fetch the element at index i (assuming i is a valid index)
    def get(self, i: int) -> int:
        return self.arr[i]

    # overwrite the value at index i to n (assuming i is a valid index)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # push the element n to the end of array
    def pushback(self, n: int) -> None:
        # check if size is equal to capacity, then we have no space
        # to accomodate any element
        if self.size == self.capacity:
            self.resize()
        # store the element at the last index
        self.arr[self.size] = n
        # increment the size by 1
        self.size += 1        

    # pop and return the last element
    def popback(self) -> int:
        # decrement the size
        self.size -= 1
        # return the last element
        return self.arr[self.size]

    def resize(self) -> None:
        # double the capacity
        self.capacity = self.capacity * 2
        # create a new arr with double capacity
        newArr = [0] * self.capacity
        # cp the element from prev array to new arr
        for i in range(len(self.arr)):
            newArr[i] = self.arr[i]
        # assign the new array to prev array
        self.arr = newArr

    # return the number of elements in the array
    def getSize(self) -> int:
        return self.size

    # return the capacity of the array
    def getCapacity(self) -> int:
        return self.capacity