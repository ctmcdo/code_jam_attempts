# Cody-Jamal's latest artistic installment is a tiled kitchen floor that can be
# retiled to different patterns. The floor consists of a matrix of R rows and C
# columns of square tiles. Each tile is reversible, one side is magenta and the
# other one is green.
#
# To retile the kitchen, there are two allowed operations:
#
#    flip a tile, changing its visible color from magenta to green, or vice versa,
#     and
#    swap two adjacent tiles (horizontally or vertically, but not diagonally),
#     without flipping either.
#
# Viewing Cody-Jamal's artistic floor is free, but interacting with it is not.
# Performing a single flip operation costs F coins, and performing a single swap
# operation costs S coins.
#
# You can see the current state of the floor and want to turn it into a particular
# pattern. What is the minimum amount of coins you need to spend to achieve your goal?

from scipy.optimize import linear_sum_assignment


def get_cost_matrix(s, d):
    global C, F, S
    cost_matrix = []
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if s[i][j] == 0:
                continue
            cost_matrix.append([])
            for k in range(0, len(s)):
                for l in range(0, len(s[0])):
                    if d[k][l] == 1:
                        cost = (abs(i - k) + abs(j - l)) * S
                        if cost > 2 * F:
                            cost = 2 * F
                        cost_matrix[-1].append(cost)
    return cost_matrix


T = int(input())
for i in range(0, T):
    l = input().split()
    R = int(l[0])
    _ = int(l[1])
    F = int(l[2])
    S = int(l[3])

    m = {"M": 0, "G": 1}

    num_source_1s = 0
    source = []
    for j in range(0, R):
        l = input()
        source.append([])
        for k in range(0, len(l)):
            L = int(m[l[k]])
            source[j].append(L)
            num_source_1s += L

    num_destination_1s = 0
    destination = []
    for j in range(0, R):
        l = input()
        destination.append([])
        for k in range(0, len(l)):
            L = int(m[l[k]])
            destination[j].append(L)
            num_destination_1s += L

    if num_source_1s == 0 or num_destination_1s == 0:
        cost_ = (num_source_1s + num_destination_1s) * F

    else:
        cost_matrix_ = get_cost_matrix(source, destination)
        row_ind, col_ind = linear_sum_assignment(cost_matrix_)
        cost_ = abs(num_source_1s - num_destination_1s) * F
        for j in range(0, len(row_ind)):
            cost_ += cost_matrix_[row_ind[j]][col_ind[j]]

    print("Case #{}: {}".format(i + 1, cost_))
