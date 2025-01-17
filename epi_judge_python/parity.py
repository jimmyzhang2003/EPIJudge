from test_framework import generic_test


def parity(x: int) -> int:
    # res = 0

    # while x:
    #     res ^= 1
    #     x &= x - 1 # equals x with its lowest set bit erased, so we can skip the intermediate 0s

    # return res

    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    
    return x & 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
