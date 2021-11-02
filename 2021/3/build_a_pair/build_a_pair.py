# You must use every digit in the list exactly once, but you get to choose which
# ones to use for the first integer and which ones to use for the second integer.
# You also get to choose the order of the digits within each integer, except you
# cannot put a zero as the most significant (leftmost) digit in either integer.
# Note that you cannot choose just a zero for one integer either, because it would
# not be positive.
#
# For example, you could be given the list [1,0,2,0,4,3]. Two of the valid pairs
# you can build are (200,143) and (3,12400). The following pairs, on the other hand,
# are not valid:

# (0102,34): has a leading zero.
# (0,12340): has a non-positive integer.
# (10,243) and (12300,47): the list of digits in each of these pairs is not exactly
# equal to the given list of digits.
#
# Given the list of digits to use, what is the minimum absolute difference between
# the two built integers that can be achieved?

import bisect
from collections import defaultdict
import sys


def min_nonzero_digit(D):
    min_d = 9
    for d in D:
        if d < min_d and d != 0:
            min_d = d
    return min_d


def min_max_even(D):
    mmin = "".join(str(d) for d in D[0 : len(D) // 2])
    max_half = [str(d) for d in D[len(D) // 2 : len(D)]]
    max_half.reverse()
    mmax = "".join(list(max_half))
    return mmin, mmax


def get_pairs(D):
    ddict = defaultdict(int)
    for d in D:
        ddict[d] += 1

    singles = []
    pairs = defaultdict(int)
    for d in ddict:
        if ddict[d] % 2 == 1:
            singles.append(d)
        if ddict[d] > 1:
            pairs[d] += ddict[d] // 2

    return pairs, singles


def min_nonzero_diff(D, zero_digit_allowed=True):
    md = 9
    for i in range(1, len(D)):
        if not zero_digit_allowed and (D[i] == 0 or D[i - 1] == 0):
            continue

        diff = D[i] - D[i - 1]
        if diff != 0 and diff < md:
            md = diff
    return md


def contains_nonzero_pair(pairs):
    for d in pairs:
        if d != 0 and pairs[d] > 0:
            return True
    return False


def pair_diff_with_first_digits_diff(singles, allowed_diff, leading_zero_allowed=True):
    if len(singles) == 2:
        return allowed_diff

    min_diff = sys.maxsize
    for i in range(1, len(singles)):
        if not leading_zero_allowed and (singles[i] == 0 or singles[i - 1] == 0):
            continue

        ddiff = singles[i] - singles[i - 1]
        if ddiff == allowed_diff:
            s1 = singles.pop(i)
            s2 = singles.pop(i - 1)

            mmin, mmax = min_max_even(singles)
            diff = abs(int(str(allowed_diff) + mmin) - int(mmax))
            if diff < min_diff:
                min_diff = diff

            bisect.insort(singles, s1)
            bisect.insort(singles, s2)

    return min_diff


def pair_diff(D, num_allowed_zeros):
    if len(D) % 2 == 1:
        min_non_zero_digit = min_nonzero_digit(D)
        D.remove(min_non_zero_digit)
        mmin, mmax = min_max_even(D)
        mmin = str(min_non_zero_digit) + mmin
        return int(mmin) - int(mmax)

    else:
        pairs, singles = get_pairs(D)
        if len(singles) == 0:
            return 0

        mdiff = sys.maxsize
        if len(pairs) > 0:
            # choose all pairs but one
            for p in pairs:
                pairs[p] -= 1
                if not contains_nonzero_pair(pairs):
                    pairs[p] += 1
                    continue

                bisect.insort(singles, p)
                bisect.insort(singles, p)
                diff = pair_diff_with_first_digits_diff(singles, 1)
                if diff < mdiff:
                    mdiff = diff

                singles.remove(p)
                singles.remove(p)
                pairs[p] += 1

            all_pairs_prefix = contains_nonzero_pair(pairs)
            if all_pairs_prefix:
                # choose all pairs
                diff = pair_diff_with_first_digits_diff(
                    singles, min_nonzero_diff(singles)
                )
                if diff < mdiff:
                    mdiff = diff

            # choose no pairs
            diff = pair_diff_with_first_digits_diff(
                D, min_nonzero_diff(D, False), False
            )
            if diff < mdiff:
                mdiff = diff

        else:
            diff = pair_diff_with_first_digits_diff(
                singles, min_nonzero_diff(singles, False), False
            )
            if diff < mdiff:
                mdiff = diff

        return mdiff


T = int(input())
for i in range(0, T):
    D = [int(a) for a in input()]
    D.sort()
    print("Case #{}: {}".format(i + 1, pair_diff(D, 0)))
