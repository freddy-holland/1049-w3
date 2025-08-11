from abstract_stack import Stack
from referential_array import ArrayR, T


class ArrayStack(Stack[T]):
    # For you to implement
    pass


if __name__ == "__main__":
    """
    Write a couple of tests for your code here.
    Something to get you started:
    """
    my_stack = ArrayStack(100)
    my_stack.push(10)
    print(my_stack.pop())

    # Call more functions, make sure the class is implemented right...
