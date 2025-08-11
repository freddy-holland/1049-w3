from stack.abstract_stack import Stack
from queue.referential_array import ArrayR, T

class ArrayStack(Stack[T]):

    MINIMUM_LENGTH = 1

    def __init__(self, max_length: int):
        self.array = ArrayR(max(self.MINIMUM_LENGTH, max_length))
        self.top = 0

    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack."""
        if self.is_full():
            raise Exception("Stack is full")

        self.array[self.top] = item
        self.top += 1

    def pop(self) -> T:
        """ Pops an element from the top of the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.array[self.top-1]
        self.top -= 1

        return item

    def peek(self) -> T:
        """ Pops the element at the top of the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.array[self.top-1]

        return item

    def __len__(self) -> int:
        """ Returns the number of elements in the stack."""
        return self.top

    def is_full(self) -> bool:
        """ Returns True iff the stack is full and no element can be pushed. """
        return len(self) == len(self.array)

    def clear(self):
        """ Clears all elements from the stack. """
        self.top = 0 


if __name__ == "__main__":
    """
    Write a couple of tests for your code here.
    Something to get you started:
    """
    my_stack = ArrayStack(100)
    my_stack.push(10)
    print(my_stack.pop())

    # Call more functions, make sure the class is implemented right...
