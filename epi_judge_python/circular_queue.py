from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self._entries = [0] * capacity
        self._head = self._tail = self._num_queue_elements = 0

        return

    def enqueue(self, x: int) -> None:
        # Check if resize is needed
        if self._num_queue_elements == len(self._entries):
            # Flattening
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [0] * (len(self._entries) * (Queue.SCALE_FACTOR - 1))

        # Adding element (From the right)
        # access_index = self._tail % len(self._entries)
        # see: https://www.snellman.net/blog/archive/2016-12-13-ring-buffers/
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

        return

    def dequeue(self) -> int:
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        target = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)

        return target

    def size(self) -> int:
        return self._num_queue_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
