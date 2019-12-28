from utils.test_case import TestCase

INPUT = """
<x=-8, y=-18, z=6>
<x=-11, y=-14, z=4>
<x=8, y=-3, z=-10>
<x=-2, y=-16, z=1>
"""

TEST_CASES = [
    TestCase("""
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
|10""", 179),
    TestCase("""
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
|100""", 1940)
]


def print_moons(step, moons):
    print("After %d steps" % step)
    for moon in moons:
        print("pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>" % (*moon[0], *moon[1]))
    print()


def solve(input, steps):
    moons = []
    for line in input.strip().split('\n'):
        coords = [int(coord.split('=')[1]) for coord in line[1:-1].split(', ')]
        moons.append([coords] + [[0, 0, 0]])
    N = len(moons)

    for step in range(steps):
        # print_moons(step, moons)
        # apply gravity
        for m1 in range(N):
            for m2 in range(m1 + 1, N):
                moon1 = moons[m1]
                moon2 = moons[m2]
                for i, (coord1, coord2) in enumerate(zip(moon1[0], moon2[0])):
                    gravity = 1 if coord1 < coord2 else -1 if coord1 > coord2 else 0
                    moon1[1][i] += gravity
                    moon2[1][i] -= gravity
        # apply velocity
        for moon in moons:
            for i in range(3):
                moon[0][i] += moon[1][i]

    print_moons(step + 1, moons)

    # calculate energy
    energy = sum(
        sum(abs(c) for c in moon[0]) * sum(abs(c) for c in moon[1])
        for moon in moons
    )
    return energy


if __name__ == '__main__':
    for case in TEST_CASES:
        system, steps = case.case.strip().split('|')
        result = solve(system, int(steps))
        case.check(result)

    print(solve(INPUT, 1000))
