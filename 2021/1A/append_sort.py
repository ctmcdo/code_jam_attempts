# We have a list of integers X_1,X_2,…,X_N. We would like them to be in strictly
# increasing order, but unfortunately, we cannot reorder them. This means that
# usual sorting algorithms will not work.
#
# Our only option is to change them by appending digits 0 through 9 to their right
# (in base 10). For example, if one of the integers is 10, you can turn it into
# 100 or 109 with a single append operation, or into 1034 with two operations (as
# seen in the image below).
#
# Given the current list, what is the minimum number of single digit append
# operations that are necessary for the list to be in strictly increasing order?
#
# For example, if the list is 100,7,10, we can use 4 total operations to make it
# into a sorted list, as the following image shows.


def fill_integer(c, p):
    for i in range(0, len(c)):
        if c[i] == p[i]:
            continue

        if c[i] > p[i]:
            for _ in range(len(c), len(p)):
                c.append(0)
        else:
            for _ in range(len(c), len(p) + 1):
                c.append(0)

        return

    incremented = False
    for i in range(len(c), len(p)):
        if not incremented and p[i] != 9:
            c.append(p[i] + 1)
            incremented = True
        else:
            c.append(0)

    if not incremented:
        c.append(0)


def num_append_digits(X):
    num_digits = 0

    prev_digits = [int(x) for x in X[0]]
    for i in range(1, len(X)):
        curr_digits = [int(x) for x in X[i]]

        if len(X[i]) <= len(prev_digits):
            num_input_digits = len(curr_digits)
            fill_integer(curr_digits, prev_digits)

            num_digits += len(curr_digits) - num_input_digits

        prev_digits = curr_digits

    return num_digits


T = int(input())
for i_ in range(T):
    _ = input()
    integers = input().split()
    print("Case #{}: {}".format(i_ + 1, num_append_digits(integers)))
