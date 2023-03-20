from test_framework import generic_test


def parity(x: int) -> int:
    res = 0
    while x:
        x = x & (x-1)
        res = res ^ 1

    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
