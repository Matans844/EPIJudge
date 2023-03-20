import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # First division: Smaller than pivot
    pivot = A[pivot_index]
    next_smaller = 0
    next_equal = 0
    next_larger = len(A) - 1

    while next_equal < next_larger:
        if A[next_equal] < pivot:
            A[next_equal], A[next_smaller] = A[next_smaller], A[next_equal]
            next_equal += 1
            next_smaller += 1
        elif A[next_equal] == pivot:
            next_equal += 1
        else:
            A[next_larger], A[next_equal] = A[next_equal], A[next_larger]
            next_larger -= 1

    if A[next_equal] < pivot:
        A[next_equal], A[next_smaller] = A[next_smaller], A[next_equal]

    return


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

def test_case_2():
    array = [0, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 2, 2, 1, 0, 2, 0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2]
    pivot_idx = 52
    dutch_flag_partition(pivot_idx, array)


if __name__ == '__main__':
    # test_case_2()
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

