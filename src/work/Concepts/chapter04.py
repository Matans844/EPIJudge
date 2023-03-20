import math


def find_lowest_set_bit(x):
    return x & ~(x - 1)


def find_index_lowest_set_bit(x):
    assert x > 0
    lsb = find_lowest_set_bit(x)
    lsb_to_index = math.trunc(math.log2(lsb))
    return lsb_to_index


def find_index_highest_set_bit(x: int) -> int:
    index = -1
    while x:
        index += 1
        x >>= 1

    return index


def isolate_bit_index(x, i):
    bit_set = 1 << i
    return x & bit_set


def extract_mask_bits(x, mask):
    return x & mask


def isolate_bit_index(x, i):
    bit_set = 1 << i
    return x & bit_set


def zero_bit_by_index(x, index):
    return x & (~(1 << index))


def create_bit_mask_ones(n):
    return (1 << n) - 1


def calculate_number_digits_in_number_by_base(x, base):
    return math.floor(math.log(x, base)) + 1
