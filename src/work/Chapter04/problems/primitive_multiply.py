from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    target = 0b0
    bit_mask = 0b1
    index = 0

    while y:
        if y & bit_mask:
            target = add_with_constraint(target, x << index)
        y >>= 1
        index += 1

    return target


def add_with_constraint(x: int, y: int) -> int:
    target = 0b0
    carry = 0
    bit_mask = 0b1
    index = 0

    while x or y:
        # Part 1: Debugging
        # print(f'start iter: target is {bin(target)}')
        # print(f'carry is {carry}')
        # print(f'x is {bin(x)}')
        # print(f'y is {bin(y)}')
        # print()

        # Part 2: Calculations
        a = x & bit_mask
        b = y & bit_mask
        if a and b:
            curr_digit = 1 if carry else 0
            carry = 1
        elif a or b:
            curr_digit = 0 if carry else 1
            # carry remains the same:
            # if carry:
            #    curr_digit = 0
            #    carry = 1
            # else:
            #    curr_digit = 1
            #    carry = 0
        else:
            curr_digit = 1 if carry else 0
            carry = 0

        # Part 3: Update
        target |= (curr_digit << index)

        # Part 4: Preparation for next iteration
        x >>= 1
        y >>= 1
        index += 1

    if carry:
        curr_digit = carry
        target |= (curr_digit << index)

    return target


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
