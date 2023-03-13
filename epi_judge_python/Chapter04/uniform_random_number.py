import functools
import math
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import Concepts.chapter04


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    # We have candidates from 1 to the number of candidates (higher-lower+1)
    n = upper_bound - lower_bound + 1

    # We check if n is a power of 2
    index_lsb = Concepts.chapter04.find_index_lowest_set_bit(n)
    index_hsb = index_lsb
    if Concepts.chapter04.zero_bit_by_index(n, index_lsb) != 0:
        index_hsb = Concepts.chapter04.find_index_highest_set_bit(n)
    greatest_power_of_2 = 1 << (index_hsb + 1)

    # Finding valid winner
    winner = -1
    while not 1 <= winner <= n:
        winner = random_binary_select(greatest_power_of_2)
        # print(winner)

    return winner + lower_bound - 1


def random_binary_select(power_2):
    left = 1
    right = power_2
    result = -1
    while left < right:
        mid = (right - left) // 2 + left
        if zero_one_random() == 1:
            # Choose right
            left = mid + 1
        else:
            # Choose left
            right = mid
    assert right == left
    result = left

    return result

    # We have a winner when we have exactly 1 set bit in the mask
    # The winning number is the 1 plus the index corresponding to that lowest set bit
    mask = (1 << n) - 1
    counter_disqualified = 0
    index = 0



@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
