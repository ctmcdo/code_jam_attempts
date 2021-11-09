# We have a matrix of square cells with R rows and C columns. We need to draw a
# diagonal in each cell. Exactly one of two possible diagonals must be drawn in
# each cell: the forward slash diagonal, which connects the bottom-left and the
# top-right corners of the cell, or the backslash diagonal, which connects the
# top-left and the bottom-right corners of the cell.
#
# For each row and column, we want to draw a specific number of diagonals of each
# type. Also, after all the diagonals are drawn, the matrix should be square free.
# That is, there should be no squares formed using the diagonals we added.
#
# Given the size of the matrix and the exact number of forward slash diagonals
# that must be drawn in each row and column, produce any square free matrix that
# satisfies the row and column constraints, or say that one does not exist.

def forms_three_sides_of_square(grid, r, c, length):
    c += 1
    for i in range(0, length):
        r -= 1
        c -= 1
        if grid[r][c] != '\\':
            return False
    
    r -= 1
    for i in range(0, length):
        r += 1
        c -= 1
        if grid[r][c] != '/':
            return False
    
    c -= 1
    for i in range(0, length):
        r += 1
        c += 1
        if grid[r][c] != '\\':
            return False

    return True


def forms_square(grid, r, c):
    max_side_length = min(c, len(grid[0]) - c, (1 + r) // 2)

    if forms_three_sides_of_square(grid, r, c, 1):
        return True

    for side_length in range(2, max_side_length + 1):
        r -= 1
        c += 1

        if grid[r][c] != '/':
            return False

        if forms_three_sides_of_square(grid, r, c, side_length):
            return True

    return False


def square_free(row_constraints, column_constraints):
    R = len(row_constraints)
    C = len(column_constraints)

    grid = [['0'] * C for i in range(0, R)]
    column_still_required = column_constraints.copy()
    row_still_required = row_constraints.copy()

    r, c = 0, 0
    while 0 <= r < R:
        direction = 0
        if grid[r][c] == '0':
            if (
                row_still_required[r] > 0
                and column_still_required[c] > 0
                and not forms_square(grid, r, c)
            ):
                grid[r][c] = "/"
                direction = 1
                column_still_required[c] -= 1
                row_still_required[r] -= 1

            elif (
                ((C - 1) - c) - row_still_required[r] >= 0
                and ((R - 1) - r) - column_still_required[c] >= 0
            ):
                grid[r][c] = "\\"
                direction = 1

        elif grid[r][c] == '/':
            if ((C - 1) - c) - (row_still_required[r] + 1)  >= 0 and ((R - 1) - r) - (
                column_still_required[c] + 1
            ) >= 0:
                grid[r][c] = "\\"
                direction = 1

            else:
                grid[r][c] = '0'

            column_still_required[c] += 1
            row_still_required[r] += 1

        else:
            grid[r][c] = '0'

        if direction == 0:
            if c > 0:
                c -= 1
            else:
                r -= 1
                c = C - 1
        else:
            if c < C - 1:
                c += 1
            else:
                r += 1
                c = 0

    return grid if r == len(row_constraints) else None


T = int(input())
for i in range(0, T):
    R = int(input().split()[0])
    row_constraints = [int(c) for c in input().split()]
    column_constraints = [int(c) for c in input().split()]
    sf = square_free(row_constraints, column_constraints)
    if sf is not None:
        print("Case #{}: POSSIBLE".format(i + 1))
        for sfrow in sf:
            print("".join(sfrow))
    else:
        print("Case #{}: IMPOSSIBLE".format(i + 1))
