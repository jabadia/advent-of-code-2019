import math
from collections import defaultdict
from math import atan2

from utils.test_case import TestCase

INPUT = """
#.#....#.#......#.....#......####.
#....#....##...#..#..##....#.##..#
#.#..#....#..#....##...###......##
...........##..##..##.####.#......
...##..##....##.#.....#.##....#..#
..##.....#..#.......#.#.........##
...###..##.###.#..................
.##...###.#.#.......#.#...##..#.#.
...#...##....#....##.#.....#...#.#
..##........#.#...#..#...##...##..
..#.##.......#..#......#.....##..#
....###..#..#...###...#.###...#.##
..#........#....#.....##.....#.#.#
...#....#.....#..#...###........#.
.##...#........#.#...#...##.......
.#....#.#.#.#.....#...........#...
.......###.##...#..#.#....#..##..#
#..#..###.#.......##....##.#..#...
..##...#.#.#........##..#..#.#..#.
.#.##..#.......#.#.#.........##.##
...#.#.....#.#....###.#.........#.
.#..#.##...#......#......#..##....
.##....#.#......##...#....#.##..#.
#..#..#..#...........#......##...#
#....##...#......#.###.#..#.#...#.
#......#.#.#.#....###..##.##...##.
......#.......#.#.#.#...#...##....
....##..#.....#.......#....#...#..
.#........#....#...#.#..#....#....
.#.##.##..##.#.#####..........##..
..####...##.#.....##.............#
....##......#.#..#....###....##...
......#..#.#####.#................
.#....#.#..#.###....##.......##.#.
"""

TEST_CASES = [
    TestCase("""
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##|11,13
""", 802),
]


def solve(input, center):
    asteroids = set()
    for y, line in enumerate(input.strip().split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                asteroids.add((x, y))

    asteroids.remove(center)
    seen_asteroids = defaultdict(list)
    for other in asteroids:
        angle = atan2((other[0] - center[0]), -(other[1] - center[1]))
        if angle < 0:
            angle += math.pi * 2
        dist = (other[1] - center[1]) ** 2 + (other[0] - center[0]) ** 2
        seen_asteroids[angle].append((dist, other))

    seen_asteroids = dict(seen_asteroids)
    for angle, dist_asteroid_pairs in seen_asteroids.items():
        seen_asteroids[angle] = sorted(dist_asteroid_pairs)

    count = 0
    i = 0
    angles = sorted(list(seen_asteroids.keys()))
    while count < 200:
        angle = angles[i % len(angles)]
        while len(seen_asteroids[angle]) == 0:
            i += 1
            angle = angles[i % len(angles)]
        vaporized = seen_asteroids[angle].pop(0)
        dist, coords = vaporized
        # print(count + 1, coords)
        if count == 199:
            return coords[0] * 100 + coords[1]
        count += 1
        i += 1

    return None


if __name__ == '__main__':
    for case in TEST_CASES:
        asteroids, center = [part.strip() for part in case.case.split('|')]
        center = tuple(map(int, center.split(',')))
        result = solve(asteroids, center)
        case.check(result)

    print(solve(INPUT, (20, 20)))
