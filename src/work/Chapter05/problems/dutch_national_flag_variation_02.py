# import functools
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class TraversalPointers:
    smaller: int
    equal: int
    larger: int


def dutch_flag_partition_index(pivot_index: int, A: List[int]) -> None:
    return dutch_flag_partition_value(A[pivot_index], A)


def dutch_flag_partition_value(pivot: int, A: List[int]) -> None:
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

# Notice that the same note from the solution to variation 01 applies here:
# - We should be dealing with `n` different objects, all of which have keys.
# - The number of keys is constant.
# The required modifications are discussed in the `dutch_national_flag_variation_01.py` file.

# When we choose the second the smallest element, we know that:
# 1. Bottom part of the array is fixed.
# 2. Chosen element subarray is also fixed.
# Hence, we only need to take care of the upper part of the array.
# Choosing the next minimum key as pivot will do the following:
# 1. leave the prefix of the array fixed, and sorted, as required.
# 2. will fix the upper part, as needed.
def dutch_flag_partition_variation02_attempt01(array: List[int]) -> None:
    keys = set(array)
    keys.remove(min(keys))
    pivot1 = min(keys)
    keys.remove(pivot1)
    pivot2 = min(keys)
    dutch_flag_partition_value(pivot1, array)
    dutch_flag_partition_value(pivot2, array)


def test_case_1():
    array = [0, 2, 1, 1, 3, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2, 3, 3]
    dutch_flag_partition_variation02_attempt01(array)
    print(array)


if __name__ == '__main__':
    test_case_1()
