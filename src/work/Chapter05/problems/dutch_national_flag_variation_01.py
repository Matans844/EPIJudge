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


def dutch_flag_partition(pivot_index: int, array: List[int], ordering: Tuple) -> None:
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
    dutch_flag_partition(pivot_idx, array, (2, 1, 0))
    print(array)


def test_case_2():
    array = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    pivot_idx = 8
    dutch_flag_partition(pivot_idx, array, (2, 0, 1))
    print(array)


if __name__ == '__main__':
    # test_case_1()
    test_case_2()
