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
.#..#
.....
#####
....#
...##
""", 8),
]


def solve(input):
    asteroids = set()
    for y, line in enumerate(input.strip().split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                asteroids.add((x, y))

    max_asteroids = 0
    for candidate in asteroids:
        seen_asteroids = len(
            set(atan2(other[1] - candidate[1], other[0] - candidate[0]) for other in asteroids if other != candidate))
        if seen_asteroids > max_asteroids:
            max_asteroids = seen_asteroids
            print(candidate, seen_asteroids)
    return max_asteroids


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
