from test_framework import generic_test


def swap_bits(x, i, j):
    upper = max(i, j)
    lower = min(i, j)

    # Getting the upper bit and zeroing it in x
    bit_upper = isolate_bit_index(x, upper)
    x = extract_mask_bits(x, ~bit_upper)

    # Getting the lower bit and zeroing it in x
    bit_lower = isolate_bit_index(x, lower)
    x = extract_mask_bits(x, ~bit_lower)

    # We need to shift between the upper bit and the lower bit in bit_upper, bit_lower
    shift_factor = upper - lower
    bit_lower = bit_lower << shift_factor
    bit_upper = bit_upper >> shift_factor

    # Shift is complete: We stitch the shifted bits together and stitch it to x
    shifted_bits = bit_lower | bit_upper
    x = x | shifted_bits

    return x


def isolate_bit_index(x, i):
    bit_set = 1 << i
    return x & bit_set


def extract_mask_bits(x, mask):
    return x & mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
