import sys


def convert_to_digits(max_coins, p):
    ret0 = []
    max_coins_arr = max_coins.copy()
    max_coins_arr.reverse()
    max_val = p

    for t in max_coins_arr:
        a = max_val % (t + 1)
        max_val = int(max_val / (t + 1))
        ret0.append(a)
        if max_val == 0:
            break

    while len(ret0) < len(max_coins_arr):
        ret0.append(0)
    ret0.reverse()

    return ret0


def brute_force_change(m, coins):
    coins_list = []
    for c in coins:
        max_c = int(m / c)
        coins_list.append(max_c)

    max_val = 1
    for max_val in coins_list:
        max_val = max_val * (max_val + 1)
    smallest_num_of_coins = sys.maxsize
    best_change = []

    for k in range(max_val):
        nums = convert_to_digits(coins_list, k)
        val = 0
        for w in range(len(nums)):
            val = val + (nums[w] * coins[w])

        if val == m:
            d = 0
            for c in nums:
                d = d + c
            if d < smallest_num_of_coins:
                smallest_num_of_coins = d
                best_change = nums

    print()
    print("Smallest number of coins: " + str(smallest_num_of_coins))
    print("Best change: " + str(best_change))


input_m = int(input("Enter amount of money: "))
input_c = input("Enter amount of coins: ")
input_c = input_c.split()

for i in range(len(input_c)):
    input_c[i] = int(input_c[i])

brute_force_change(input_m, input_c)
