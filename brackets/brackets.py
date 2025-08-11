asdfrom array_stack import ArrayStack


def is_balanced(some_string: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    """
    Test your code here...
    """

    assert is_balanced("()") == True   # Is the comparison to True necessary?
    assert is_balanced(")(") == False  # How about comparison to False?

    # Add more tests...
