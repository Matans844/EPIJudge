from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    target = 0b0
    if x & 1:
        lowest_non_set_bit = find_lowest_set_bit(~x)
        target = x + (lowest_non_set_bit >> 1)

    else:
        lowest_non_set_bit = find_lowest_set_bit(x)
        target = x - (lowest_non_set_bit >> 1)

    return target


def find_lowest_set_bit(x):
    return x & ~(x - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
