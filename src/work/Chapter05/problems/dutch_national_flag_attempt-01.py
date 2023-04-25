import functools
from typing import List

from test.test_framework.test_failure import TestFailure
from test.test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # First division: Smaller than pivot
    pivot = A[pivot_index]
    next_left = dutch_flag_binary_partition(pivot, A, 0, len(A)-1, lambda x: x < pivot)

    dutch_flag_binary_partition(pivot, A, next_left, len(A)-1, lambda x: x == pivot)

    return


def dutch_flag_partition_book_2(pivot_index, array):
    pivot = array[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[smaller] = array[smaller], array[i]
            smaller += 1
    # Second pass: group elements larger than pivot
    larger = len(array)-1
    for i in reversed(range(len(array))):
        if array[i] < pivot:
            break
        elif array[i] > pivot:
            array[i], array[larger] = array[larger], array[i]
            larger -= 1


def dutch_flag_binary_partition(pivot, array, left, right, deciding_function):
    next_true = left
    next_false = right

    while next_true < next_false:
        if deciding_function(array[next_true]):
            next_true += 1
        else:
            array[next_true], array[next_false] = array[next_false], array[next_true]
            next_false -= 1

    if deciding_function(array[next_true]):
        next_true += 1

    return next_true


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


def test_case_1():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    pivot_idx = 8
    dutch_flag_partition(pivot_idx, array)


# This test fails
def test_case_2():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    pivot_idx = 1
    dutch_flag_partition(pivot_idx, array)
    print(array)


def test_case_3():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    pivot_idx = 1
    dutch_flag_partition_book_2(pivot_idx, array)
    print(array)


if __name__ == '__main__':
    test_case_2()
    test_case_3() # The question is not about sorting, but about partition!!!!!

    '''
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
    '''

