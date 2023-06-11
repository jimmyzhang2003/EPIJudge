from test_framework import generic_test


def power(x: float, y: int) -> float:
    ans, pow = 1.0, y

    if y < 0:
        pow, x = -pow, 1/ x

    while pow:
        if pow & 1:
            ans *= x
        
        x, pow = x * x, pow >> 1

    return ans

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
