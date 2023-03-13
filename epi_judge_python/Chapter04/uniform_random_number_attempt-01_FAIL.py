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

    # We have a winner when we have exactly 1 set bit in the mask
    # The winning number is the 1 plus the index corresponding to that lowest set bit
    mask = (1 << n) - 1
    counter_disqualified = 0
    index = 0

    while counter_disqualified < n - 1:
        if zero_one_random() == 0:
            counter_disqualified += 1
            mask = Concepts.chapter04.zero_bit_by_index(mask, index)

        # Determining next index position
        shift_factor = index + 1
        mask_left_of_index = mask >> shift_factor
        if mask_left_of_index:
            index = Concepts.chapter04.find_index_lowest_set_bit(mask_left_of_index) + shift_factor
        else:
            index = Concepts.chapter04.find_index_lowest_set_bit(mask)

    winner = Concepts.chapter04.find_index_lowest_set_bit(mask) + lower_bound
    # print(winner)

    return winner


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
