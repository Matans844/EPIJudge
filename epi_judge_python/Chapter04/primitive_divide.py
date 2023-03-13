from test_framework import generic_test


def divide(x: int, y: int) -> int:
    index_set_msb_x = find_index_highest_set_bit(x)
    index_set_msb_y = find_index_highest_set_bit(y)
    size_y = index_set_msb_y+1
    index = index_set_msb_x - index_set_msb_y
    answer = 0b0
    answer_sum = 0b0

    while index >= 0:
        # x/y = k = ( k_1* (2^(index_1)) + ... k_n* (2^(index_2))
        # x = y * ( k_1* (2^(index_1)) + ... k_n* (2^(index_2)) )

        candidate_bit = 1 << index
        candidate_answer = answer | candidate_bit

        candidate_addition = y << index
        candidate_sum = answer_sum + candidate_addition

        if candidate_sum == x:
            answer = candidate_answer
            break

        elif candidate_sum < x:
            answer = candidate_answer
            answer_sum = candidate_sum

        index -= 1

    return answer


def find_index_highest_set_bit(x: int) -> int:
    index = -1
    while x:
        index += 1
        x >>= 1

    return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
