# You are playing a new solitaire game called Prime Time. You are given a deck of
# cards, and each card has a prime number written on it. Multiple cards may have
# the same number.
#
# Your goal is to divide the cards into two groups in such a way that the sum of
# the numbers in the first group is equal to the product of the numbers in the
# second group. Each card must belong to exactly one of the two groups, and each
# group must contain at least one card. The sum or product of a group that consists
# of a single card is simply the number on that card.
#
# For example, in the image above, the left group has cards whose sum is 25 and
# the right group has cards whose product is 25. Therefore, this is a valid split
# into groups.
#
# Your score is the sum of the numbers in the first group (which is equal to the
# product of the numbers in the second group), or 0 if you cannot split the cards
# this way at all. What is the maximum score you can achieve?

from collections import defaultdict
import math


primes = []
for num in range(2, 500):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

# times 2 for good measure.
# intuitively 499 * (int(math.log(10 ** 15, 499)) + 1) shouldn't be
# more than a couple of hundred off maybe
sum_range = 499 * (int(math.log(10 ** 15, 499)) + 1) * 2


def prime_factors(n):
    pfactors = defaultdict(int)
    while n % 2 == 0:
        pfactors[2] += 1
        n = n // 2

    for i in range(3, min(int(math.sqrt(n)) + 1, 500), 2):
        while n % i == 0:
            pfactors[i] += 1
            n = n // i

    if n > 499:
        return None
    else:
        if n != 1:
            pfactors[n] += 1
        return pfactors


def factor_sum(pfactors, primes_input):
    factor_sum = 0
    for factor in pfactors:
        factor_sum += factor * pfactors[factor]
        if factor not in primes_input or primes_input[factor] < pfactors[factor]:
            return None
    return factor_sum


def largest_product_sum(primes_input, s):
    for i in range(s, max(s - sum_range - 1, 0), -1):
        pfactors = prime_factors(i)
        if pfactors is not None:
            fs = factor_sum(pfactors, primes_input)
            if fs is not None:
                if s - fs == i:
                    return i
    return 0


T = int(input())
for i in range(T):
    M = int(input())

    s = 0
    primes = {}
    for j in range(M):
        PN = input().split()
        primes[int(PN[0])] = int(PN[1])
        s += int(PN[0]) * int(PN[1])

    print("Case #{}: {}".format(i + 1, largest_product_sum(primes, s)))
