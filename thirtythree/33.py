from thirtythree.decompositions import weak_decompose, Node
from collections import namedtuple
from operator import mul


'''
This constitutes a search through 3-space for a coordinate satisfying

x^3 + y^3 + z^3 = 33

Immediately we know there are no all positive or negative solutions, by brute force and a smidge of sense. This removes a fourth of the search space. There is no 2-dimensional solution, but the optimization advantage of this is vanishingly small as you traverse 3-space.

Then we are interested in a solution such that one or two of these indices are negative.

Further, we can restrict our search (without complicating traversal code) by eliminating all solutions such that the combination of the modulus of their cubes results in 0 mod 33:

32^3 = 32678
1^3 = 1
0^3 = 0

The third argument to pow is actually the modulus.
pow(32768 + 1 - 0, 1, 33) => 0

One thing to note here is that 32^3 mod 33 := 32 mod 33, this does not hold generally:
expt(7, 3, 33) => 13

But it is a surjective function from the least residue system (or any complete residue system) of 33 to the least residue system (denoted LRS) of 33, and if we restrict our input to the LRS, then it is a bijection between the LRS to itself! This again does not hold generally.

We are going to capture all the permutations in our enumeration function. Then we are free to assume any offset is permuted, and can eliminate restrictions this way.

Further we will generate the offsets for a sign and negate them, the arguments are the same either way.
'''  # noqa: E501

K = 33

def zip_offsets(unsigned_offset, signs):
    return tuple(off * sign for off, sign in zip(unsigned_offset, signs))


CASE_ONE_UNSIGNED = []
for i in reversed(range(K)):
    for decomp in weak_decompose(i, 2):
        CASE_ONE_UNSIGNED.append((i, *decomp))

# case: (+, -, -)
CASE_ONE_SIGNAGE = (1, -1, -1)
CASE_ONE = tuple(
    zip_offsets(unsigned, CASE_ONE_SIGNAGE)
    for unsigned in CASE_ONE_UNSIGNED)

# negative case: (-, +, +)
CASE_ONE_NEG_SIGNAGE = (-1, 1, 1)
CASE_ONE_NEG = tuple(
    zip_offsets(unsigned, CASE_ONE_NEG_SIGNAGE)
    for unsigned in CASE_ONE_UNSIGNED)


CASE_TWO_UNSIGNED = []
for i in reversed(range(K)):
    CASE_TWO_UNSIGNED.append((i, i, 0))

# case: (+, -, +)
CASE_TWO_SIGNAGE = (1, -1, 1)
CASE_TWO = tuple(
    zip_offsets(unsigned, CASE_TWO_SIGNAGE)
    for unsigned in CASE_TWO_UNSIGNED)

# case: (-, +, -)
CASE_TWO_NEG_SIGNAGE = (-1, 1, -1)
CASE_TWO_NEG = tuple(
    zip_offsets(unsigned, CASE_TWO_NEG_SIGNAGE)
    for unsigned in CASE_TWO_UNSIGNED)


# case three is the most complicated.
# I believe the solution is to filter everything less than i, and
# subtract i from the elements of the decomposition. but I haven't
# worked it out on paper quite yet.
CASE_THREE_UNSIGNED = []
for i in range(65, 32, -1):
    for decomp in weak_decompose(i, 2):
        pass

# case: (+, +, -)
CASE_THREE_SIGNAGE = (1, 1, -1)
CASE_THREE = tuple(
    zip_offsets(unsigned, CASE_THREE_SIGNAGE)
    for unsigned in CASE_THREE_UNSIGNED)


