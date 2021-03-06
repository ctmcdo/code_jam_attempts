# Cody-Jamal is working on his latest piece of abstract art: a mural consisting
# of a row of waning moons and closed umbrellas. Unfortunately, greedy copyright
# trolls are claiming that waning moons look like an uppercase C and closed
# umbrellas look like a J, and they have a copyright on CJ and JC. Therefore, for
# each time CJ appears in the mural, Cody-Jamal must pay X, and for each time JC
# appears in the mural, he must pay Y.
#
# Cody-Jamal is unwilling to let them compromise his art, so he will not change
# anything already painted. He decided, however, that the empty spaces he still
# has could be filled strategically, to minimize the copyright expenses.
#
# For example, if CJ?CC? represents the current state of the mural, with C
# representing a waning moon, J representing a closed umbrella, and ? representing
# a space that still needs to be painted with either a waning moon or a closed
# umbrella, he could finish the mural as CJCCCC, CJCCCJ, CJJCCC, or CJJCCJ. The
# first and third options would require paying X+Y in copyrights, while the second
# and fourth would require paying 2⋅X+Y
#
# Given the costs X and Y and a string representing the current state of the mural,
# how much does Cody-Jamal need to pay in copyrights if he finishes his mural in a
# way that minimizes that cost?


def cost(S, X, Y):
    c = 0
    for i in range(1, len(S)):
        s1 = S[i - 1]
        s2 = S[i]
        pair = s1 + s2

        if pair == "CJ":
            c += X
        elif pair == "JC":
            c += Y
    return c


T = int(input())
for i in range(T):
    line = input()
    parts = line.split()
    S = parts[2].replace("?", "")

    if len(S) < 2:
        c = 0
    else:
        c = cost(S, int(parts[0]), int(parts[1]))

    print("Case #{}: {}".format(i + 1, c))
