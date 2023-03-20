from test_framework import generic_test
from Concepts.chapter04 import reverse


def is_palindrome_number(x: int) -> bool:
    return x >= 0 and reverse(x) == x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
