from test_framework import generic_test


def reverse(x: int) -> int:
    answer = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x:
        curr_digit = divmod(x, 10)[1]
        if answer == 0:
            answer = curr_digit
        else:
            answer = (10 * answer) + curr_digit
        x = x // 10
    return answer * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
