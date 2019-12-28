from utils.test_case import TestCase

INPUT = """
####.
.###.
.#..#
##.##
###..
"""

TEST_CASES = [
    TestCase("""
....#
#..#.
#..##
..#..
#....
""", 2129920),
]


def print_tiles(tiles, N):
    for row in range(N):
        for col in range(N):
            print(tiles[(row, col)], end='')
        print()
    print()


def move(p, m):
    return p[0] + m[0], p[1] + m[1]


def neighbours(tiles, pos):
    return [tiles.get(move(pos, delta), '.') for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]]


def next_gen(tiles, N):
    # print_tiles(tiles, N)
    next_tiles = {}
    counts = {}
    for pos, cell in tiles.items():
        count = neighbours(tiles, pos).count('#')
        counts[pos] = str(count)
        if cell == '#' and count == 1 or cell == '.' and 1 <= count <= 2:
            next_tiles[pos] = '#'
        else:
            next_tiles[pos] = '.'
    # print_tiles(counts, N)
    # print_tiles(next_tiles, N)
    return next_tiles


def rating(tiles):
    return sum(pow(2, i) for i, tile in enumerate(tiles.values()) if tile == '#')


def solve(input):
    tiles = {(row, col): v for row, line in enumerate(input.strip().split('\n')) for col, v in enumerate(line)}
    N = len(input.strip().split('\n')[0])
    # print_tiles(tiles, N)
    seen = {rating(tiles)}
    while True:
        tiles = next_gen(tiles, N)
        tiles_rating = rating(tiles)
        if tiles_rating in seen:
            return tiles_rating
        seen.add(tiles_rating)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
