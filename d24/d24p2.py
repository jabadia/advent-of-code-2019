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
#.?##
..#..
#....
""", 99),
]


def print_tiles(tiles):
    for level in range(-5, 6):
        print('level %d' % level)
        for row in range(5):
            for col in range(5):
                print(tiles.get((row, col, level),'?'), end='')
            print()
    print()


def move(p, m):
    return p[0] + m[0], p[1] + m[1], p[2] + m[2]


def neighbours(tiles, pos):
    row, col, level = pos
    ns = []

    # top neighbour
    if row == 0:
        ns.append((1, 2, level - 1))
    elif row == 3 and col == 2:
        ns.extend((4, c, level + 1) for c in range(5))
    else:
        ns.append((row - 1, col, level))

    # bottom neighbour
    if row == 4:
        ns.append((3, 2, level - 1))
    elif row == 1 and col == 2:
        ns.extend((0, c, level + 1) for c in range(5))
    else:
        ns.append((row + 1, col, level))

    # left neighbour
    if col == 0:
        ns.append((2, 1, level - 1))
    elif row == 2 and col == 3:
        ns.extend((r, 4, level + 1) for r in range(5))
    else:
        ns.append((row, col-1, level))

    # right neighbour
    if col == 4:
        ns.append((2, 3, level - 1))
    elif row == 2 and col == 1:
        ns.extend((r, 0, level + 1) for r in range(5))
    else:
        ns.append((row, col+1, level))

    return [tiles.get(n, '.') for n in ns]


def next_gen(tiles):
    next_tiles = {}
    for pos, cell in tiles.items():
        count = neighbours(tiles, pos).count('#')
        if cell == '#' and count == 1 or cell == '.' and 1 <= count <= 2:
            next_tiles[pos] = '#'
        else:
            next_tiles[pos] = '.'
    return next_tiles


def solve(input, test=False):
    tiles = {(row, col, 0): v for row, line in enumerate(input.strip().split('\n')) for col, v in enumerate(line)}
    tiles.update({(row, col, level): '.' for row in range(5) for col in range(5) for level in range(-200, 200) if level != 0})
    for level in range(-200, 200):
        del tiles[(2, 2, level)]
    for minute in range(10 if test else 200):
        tiles = next_gen(tiles)
        print(list(tiles.values()).count('#'))
    print_tiles(tiles)
    return list(tiles.values()).count('#')


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case, test=True)
        case.check(result)

    print(solve(INPUT))
