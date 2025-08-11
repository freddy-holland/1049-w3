from array_stack import ArrayStack


def is_balanced(some_string: str) -> bool:

    str_len = len(some_string)
    stack = ArrayStack(str_len)

    for char in some_string:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False

            stack.pop()

    return True

    """ Is this another option???
    open_int = 0

    for char in some_string:
        if char == "(":
            open_int += 1
        elif char == ")":
            open_int -= 1

        if open_int < 0:
            return False

    if open_int != 0:
        return False
    else:
        return True
    """

if __name__ == "__main__":
    """
    Test your code here...
    """

    assert is_balanced("()") == True   # Is the comparison to True necessary?
    assert is_balanced(")(") == False  # How about comparison to False?

    # Add more tests...
