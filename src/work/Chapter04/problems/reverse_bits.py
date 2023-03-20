from test_framework import generic_test


def reverse_bits(x: int) -> int:
    reversed_x = 0b0
    i = 0
    while x:
        reversed_x = (reversed_x << 1) | (x & 1)
        x >>= 1
        i += 1

    reversed_x <<= (64 - i)

    return reversed_x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
