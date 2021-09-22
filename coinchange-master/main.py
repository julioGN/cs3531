# general coin change project (brute-force algorithm)

import sys

d = 2
n = 2


def convert_to_digits(k):

    ret0 = []
    for t in range(d):
        a = k % (n + 1)
        ret0.append(a)
        k = int(k / (n + 1))

    ret = []
    for j in range(len(ret0) - 1, -1, -1):
        ret.append(ret0[j])
    return ret


smallest_num_of_coins = sys.maxsize

max_val = pow((n + 1), d) - 1

for i in range(max_val - 1):
    # multiply the coin times the coin value instead of print
    print(convert_to_digits(i))

