from queue.circular_queue import CircularQueue
from stack.array_stack import ArrayStack

def reverse_queue(original_queue):

    original_length = len(original_queue)
    new_stack = ArrayStack(original_length)
    new_queue = CircularQueue(original_length)

    for _ in range(original_length):
        new_stack.push(original_queue.serve())

    for _ in range(original_length):
        new_queue.append(new_stack.pop())

    return new_queue


if __name__ == "__main__":
    # As always, test your code.

    q1 = CircularQueue(8)
    q1.append(1)
    q1.append(2)
    q1.append(3)
    q1.append(4)
    q1.append(5)
    q1.append(6)
    q1.append(7)
    q1.append(8)

    q2 = reverse_queue(q1)

    for _ in range(len(q2)):
        print(q2.serve())

