from test_framework import generic_test


def power(x: float, y: int) -> float:
    result = 1
    while y:
        result = result * result
        if y & 1:
            result = result * x

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
