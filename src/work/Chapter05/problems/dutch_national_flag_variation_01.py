# import functools
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class TraversalPointers:
    smaller: int
    equal: int
    larger: int


def compare_by_ordering(x, y, ordering):
    """
    A custom comparison function that performs comparison according to a given
    precedence ordering.

    Parameters:
    - x, y: the two objects to be compared
    - ordering: a tuple containing the objects in the order of precedence,
                from highest to lowest

    Returns:
    - -1 if x < y
    - 0 if x == y
    - 1 if x > y
    """
    if x == y:
        return 0
    for i, obj in enumerate(ordering):
        if x == obj:
            return -1
        elif y == obj:
            return 1
    # if neither x nor y are in the ordering, compare their values
    return (x > y) - (x < y)


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


# Notice:
# This solution does not take into account the added complexity in the exercise, such that:
# 1. The array is composed of `n` different elements.
# 2. Each element has a key. The total number of keys is 3 (i.e., constant)
# 3. We need a solution with linear time complexity and constant space complexity.
# Our solution should go through the following modifications:
# 1. In the internal function, we compare keys of objects, not objects.
# 2. In the internal function, the natural ordering is used (we do not need to add an `ordering` tuple as I tried).
# 3. When building the set of keys, we need to iterate over the array, examining keys of each object.
def dutch_flag_partition_variation01_attempt03(array: List[int]) -> None:
    # Get unique elements from array.
    # Since there are 3 possible keys, this is constant space.
    keys = set(array)

    # Choose middle element
    keys.remove(min(keys))
    keys.remove(max(keys))
    pivot = keys.pop()

    # Use the middle element to partition
    dutch_flag_partition_value(pivot, array)


# If we knew the keys beforehand, we could choose the middle element as pivot.
# I am assuming this is not the case.
# If we choose the first index as pivot:
# 1. If it is the middle element - we are done.
# 2. If it is the highest element - we need to fix bottom part of array.
# 3. If it is the lowest element - we need to fix top part of array.
# I cannot find a good way to fix bottom part, without:
# 1. going into the array or
# 2. getting some sense on where the top part finishes.
def dutch_flag_partition_variation01_attempt02(array: List[int]) -> None:
    pivot1 = array[0]
    dutch_flag_partition_value(pivot1, array)
    if array[0] < pivot1 < array[-1]:
        # We chose middle element
        return
    elif array[0] == pivot1:
        # We need to fix upper part
        dutch_flag_partition_index(len(array) - 1, array)
    else:
        # We need to fix bottom part
        # The following is wrong...
        dutch_flag_partition_index(0, array)


# This is not a good solution.
# I have a solution that does partition, why insert `ordering` to it?
# If there's ordering involved:
# 1. Modify the data so that ordering fits the current use case
# 2. Use this function.
# 3. Modify back.
# This solution adds a layer of complexity that should better exist outside of it.
def dutch_flag_partition_variation01_attempt01(pivot_index: int, array: List[int], ordering: Tuple) -> None:
    pivot = array[pivot_index]
    pointers = TraversalPointers(0, 0, len(array))
    # smaller, equal, larger = 0, 0, len(array)
    while pointers.equal < pointers.larger:
        if compare_by_ordering(array[pointers.equal], pivot, ordering):
            array[pointers.smaller], array[pointers.equal] = array[pointers.equal], array[pointers.smaller]
            pointers.smaller, pointers.equal = pointers.smaller + 1, pointers.equal + 1
        elif compare_by_ordering(array[pointers.equal], pivot, ordering):
            pointers.equal += 1
        else:
            pointers.larger -= 1
            array[pointers.equal], array[pointers.larger] = array[pointers.larger], array[pointers.equal]


def test_case_1():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    pivot_idx = 8
    dutch_flag_partition_variation01_attempt01(pivot_idx, array, (2, 1, 0))
    print(array)


def test_case_2():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    pivot_idx = 8
    dutch_flag_partition_variation01_attempt01(pivot_idx, array, (2, 0, 1))
    print(array)


def test_case_3():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    dutch_flag_partition_variation01_attempt02(array)
    print(array)


def test_case_4():
    array = [2, 0, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    dutch_flag_partition_variation01_attempt02(array)
    print(array)


def test_case_5():
    array = [1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    dutch_flag_partition_variation01_attempt02(array)
    print(array)


def test_case_6():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    dutch_flag_partition_variation01_attempt03(array)
    print(array)


if __name__ == '__main__':
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    # test_case_5()
    test_case_6()
