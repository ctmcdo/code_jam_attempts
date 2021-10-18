#  A matryoshka is a type of doll that originated in Russia over a century ago.
#  Their defining characteristic is that they consist of a set of dolls, all of a
#  different size, with smaller dolls fitting nicely inside larger dolls.
#
# In this problem, we work with matrygons, which are sets of regular convex polygons
# that follow a similar nesting pattern. A matrygon consists of a set of regular
# convex polygons with positive area p1,p2,…,pk such that, for all i, the vertices
# of pi+1 overlap with a proper subset of the vertices of pi (pi+1 has strictly
# less vertices than pi).
#
# For example, the following pictures illustrates two matrygons. The first one
# contains 3 regular convex polygons: a regular icositetragon (24 sides), a regular
# hexagon (6 sides), and an equilateral triangle (3 sides). The second one contains
# 2 regular convex polygons: a regular icosidigon (22 sides) and a regular hendecagon
# (11 sides). Each of these matrygons has 33 total sides among all polygons in it.


def max_polygons(N, last):
    if N == 0:
        return 0

    mp = 1 if N % last == 0 and N // last > 1 else 0
    for i in range(int(last * 2), N // 2 + 1, int(last)):
        if N % i == 0:
            mp_ = max_polygons(N - i, i)
            if mp_ > 0 and mp_ + 1 > mp:
                mp = mp_ + 1

    return mp


T = int(input())
for i_ in range(0, T):
    print("Case #{}: {}".format(i_ + 1, max(1, max_polygons(int(input()), 1.5))))
