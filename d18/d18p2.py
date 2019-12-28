import heapq
from utils.test_case import TestCase

INPUT = """
#################################################################################
#.............#...#...O.#.#...........#.#...#.........#.......#.....#.......#.Z.#
#####.#######.#H#.#.###.#.#.#####.###.#.#.###.#####.#.#.#####.#.###.#.###.###.#.#
#.....#.#...#.#.#...#.#.#.#.#.#...#.....#.#...#...#.#.#...#w..#...#...#.#.....#.#
#.#####.#.#.#.#.#####.#.#.#B#.#.#########.#.###.#.#.#####.#.#####.#####.#######.#
#.#...#...#.....#...#.#.#.....#.........#.#.#...#.#.....#.#...#..y..#...#.....#.#
#.#.#.#.#########.#.#.#.###########.###.#.#.#.#######.###.###.#####.#.#.#.###.#.#
#.#.#...#.........#.#.......#.....#...#.#.#.#.#.....#.....#.#.#...#...#.#.#...#.#
#.###.###.#########.#######.#.###.#####.#.#.#.#.###.#######.#.#.#.#####.#.#.###.#
#...#.#.....#x....#.#..f..#...#...#...#.#.#.#.....#.....#i..#...#.#...#.#.#.#...#
#.#.#.#.#####.###.#.#A###.#####.###.#.#.#.#.#########.#.#.#.#####.#.#.###.#.#.#.#
#.#.#.#.#...#.#.#.#...#.#.#...#.#.T.#...#.#...#.....#.#...#.#.#..e#.#.....#.#.#.#
###.###.#X#.#.#.#.#.###.#.###.#.###.###.#.###.#.###.#.#####.#.#.###.#######.#.#.#
#...#d..#.#...#.#.#.....#...#.#...#...#.#...#.#.#.....#.......#.#.....#.#...#.#.#
#.###.###.#####R#.#####.###.#.###.###.#.#.#.#.#.###########.###.#.###.#.#.#####.#
#...#.#.#...#.......#...#...#...#.....#.#.#...#.....#.....#.#...#...#.#...#...#.#
###E#.#.###.#######.#####.###.#.#######.#.#####.###N#.###.###.###.###.#.###.#.#.#
#.#...#...#..c..#...#r..F.#...#.....#.#.#...#.#.#.#.#...#.#...#...#...#.....#.#.#
#.#####.#######.###.#.#######.#####.#.#.###.#.#.#.#.###.#.#.###.###.#########.#.#
#z....#.......#...#...#.....#s#.......#.#.#.#.....#...#.#...#v..#.#...#.....#...#
#.#.###.#.#######.#####G###.#.#######.#.#.#.#####.#.###.#######.#.###.#.#######.#
#.#.#...#.......#...#...#.#.#...#...#.#.#.#.....#.#...#.D.....#.....#.#.......#.#
###.#.#########.###C#####.#.#.#.#.#.###.#.#####.#####.###############.#.#####.#.#
#...#...#.....#...#....g....#.#.#.#.....#.....#.....#...........#.....#.....#...#
#.#####.#.###.#.#############.#.#.#######.#########.#.#######.#.#.#########.#####
#.....#...#...#.#.........#...#.#.#.....#.........#.#.#.....#.#...#.......#.#..u#
#Q#.#######.###.#.#.#.#####.###.#.#####.#.#######.#.###.###.#.#####.###.#.#.#.###
#.#.......#.#...#.#.#.#...#.#.#...#...#.#.#.....#.#.#...#.#.#...#.....#.#.#.#...#
#.#####.###.#.###.#.###.#.#.#.#####.#.#.#.#.###.#.#.#.###.#.#.#.#######.#.#.#.#.#
#...#...#...#.....#.....#...#.......#...#.#.#.#.K.#...#.#...#.#.#.......#.#.#.#.#
###.#.###.#####################.###.#####.#.#.#.#######.#.#####.#.#####.###.#.#.#
#...#.....#...#.....#.........#...#.#...#.#.#...#.......#...#...#...#...#...#.#.#
#.#########.###.###.#.###.###.###.#.#.#.###.#####.#.###.###.#.###.#.#.###.#####.#
#.#.....#.........#...#...#.#.#.#.#.#.#.#...#.....#.#l..#.#.#...#.#.#...#...#...#
#.###.#.###.###########.###.#.#.#.#.#.#.#.###.#####.#.###.#.###.#.#.#.#####.#.#.#
#.#...#...#...#...#.....#...#.#...#...#.#...#.#.#...#.....#.....#.#.#.#...#.#.#.#
#.#.#####.#.###.#.#.#####.###.#########.#.#.#.#.#.#################.###.#.#P#.#.#
#.#.#.....#.#...#.#...#.#...#.#.....#...#.#.#.#.#.#.................#...#...#.#.#
#.#.#.#######.###.###.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#########.#######.#######.#.#
#.U.#p........#....j..#...#.....#.....#@#@#.....#...........#...........J.....#.#
#################################################################################
#...#.....#...#.......#.........#......@#@#.....#.....#.....#.....#.............#
#.#.#.###.###.#.#L###.#.#####.###.#.###.#.#.#.###.#.###.#.#.#.#.#.#.#########.#.#
#.#...#.....#...#...#.#.#...#.....#...#.#...#.....#.....#.#.#.#.#.#.#.......#q#.#
#.#.#######.#.#####.#.###.#.#########.#.#.###############.###.#.#.###.#####.###.#
#.#.#.....#.#...#...#.....#.#.........#.#.#.....#.....#...#...#.#.....#...#...#.#
#.#.#.###.#.#####.#########.#.#########.#.#.#.#.#.###.#.###.###.#.#####.#.###.#.#
#.#.#...#.#.....#.....#...#...#.......#.#.#.#.#...#...#.#.....#.#.#...#.#...#...#
#.#####.#.#####.#####.#.#######.###.###.#.#.#.#####.###.#.#####.#.#.#.#.###.###.#
#.....#.#...#...#...#.#...........#...#.#k#.#...#.....#.#.#.....#.#.#.#...#...#.#
#####.#.###.###.#.#.#.#.#############.#.#.#.###.#.#####.#.#.#######.#.###.#.###.#
#.....#...#...#...#...#.#...........#...#.#...#.#...#...#.#...#...#.#...#.#.....#
#.#######.###.#####.#####.#########.#.###.#####.###.#.###.###.#.#.#.###.#.#######
#.......#...#.....#.#.....#.......#.#...#.......#.#.#.#...#.#...#.....#.#.#.....#
#.###.#####.#####.###.#####.#.#.###.#############.#.#.#.###.###########.#.#.###.#
#...#.#.........#...#.#.....#.#.#...#...#...#.....#.#...#...#.......#...#.#.#m..#
#.###.#.###########.#.#######.###.###.#.#.#.#.#.###.#####.#.#######.#.###.#.#.#.#
#.#...#...#.#.......#...#...#.W...#...#.#.#.#.#.....#.....#...#.....#...#.#.#.#.#
###.#.###.#.#.#########.#.#.#####.###.#.#.###.#######.#######.#.###.###.#.###.#.#
#...#...#...#...#.....#...#.....#...#.#.#.#...#.........#.......#.#.#...#.....#.#
#.#########.###.#.#.###########.###.#.#.#.#.###.#######.#.#######.#.#.#########.#
#.........#.#...#.#.#....a......#.#...#.#.#...#.#.......#.#...#.....#.#...#.....#
#.#######.#.#.###.#.#############.#####.#.###.#.#.#######.#.###.#####.###.#.#####
#.#.....#...#.#...#.....#...#.......#h..#.....#.#.#.......#.#...#...#...#.#.#...#
#.###.#.#####.#.#####.#.#.#.#.#####.#.###.#######.#######.#.#####.#.###.#.#.#.#.#
#...#.#...#...#.#...#.#.#.#..o#...#...#.#.......#.......#.#.....#.#.#...#.....#.#
###.#####.#.#.#.###.#.###.#######.#####.#######.#.#####.#######.#.#.#.###########
#.#...#...#.#.#.....#.....#.#.......#...#...#...#.....#.......#.#.#.#...#.......#
#.###.#.###.#.#####.#######.#.#I###.###.#.#.#.###########.###.#.#.#.###.#.#####.#
#...#...#...#.....#.#.#.....#.#...#t..#.#.#...#.........#.#.#.#...#...#...#.....#
#.#####.#.#########.#.#.###.#.###.###.#.#.#####.#######.#.#.#.#######.#####.#####
#...M...#.......#...#...#.#...#.#...#...#.......#.....#.#.#.........#.....#.#...#
#.#############.#.###.###.#####.###.#############.#####.#.#.#######.#####.#.###.#
#.#.....Y...#.#.#.#.#.#..b..#...#.#.#...#...#.........#.#.#.#...#.#.#...#...#...#
#.#.#######.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#######.#.#.###.#.#.#.#.#.#####.#.#
#...#n....#.#.#...#.......#...#...#...#.#.#.#.#.....#...#.....#.#...#.#.......#.#
#####.###.#.#.###################.#####.#.###.#.###.#####V#####.#.###.###.#####.#
#.....#...#...#.....#...#...#.....#.....#.....#...#...........#.#...#.#...#.....#
#.###########.###.#.#.#.#.#.#######.###.#.#####################.###.###.###.#####
#.................#...#...#.........#.S.#.......................#.......#.......#
#################################################################################
"""

TEST_CASES = [
    TestCase("""
#######
#a.#Cd#
##@#@##
#######
##@#@##
#cB#.b#
#######
""", 8),
    TestCase("""
###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############
""", 24),
    TestCase("""
#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############
""", 32),
    TestCase("""
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############
""", 72),
]


def find_me(vault):
    robots = []
    for y, line in enumerate(vault):
        for x, c in enumerate(line):
            if c == '@':
                robots.append((x, y))
    return robots


def collect_keys(vault):
    keys = {}
    for y, line in enumerate(vault):
        for x, c in enumerate(line):
            if is_key(c):
                keys[c] = (x, y)
    return keys


DIRECTIONS = '<^>v'


def move(pos, direction):
    x, y = pos
    if direction == '<':
        return x - 1, y
    elif direction == '^':
        return x, y - 1
    elif direction == '>':
        return x + 1, y
    elif direction == 'v':
        return x, y + 1


def get_cell(vault, pos):
    x, y = pos
    if 0 <= x < len(vault[0]) and 0 <= y < len(vault):
        return vault[y][x]
    else:
        assert False


def is_key(c):
    return 'a' <= c <= 'z'


def is_door(c):
    return 'A' <= c <= 'Z'


def options_bfs(vault, start):
    graph = {}
    visited, queue = set(), [(start, 0, set())]
    while queue:
        vertex, dist, doors = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for direction in DIRECTIONS:
                next_pos = move(vertex, direction)
                if next_pos in visited:
                    continue
                cell = get_cell(vault, next_pos)
                if cell == '#':
                    continue
                if is_key(cell):
                    graph[cell] = (dist + 1, next_pos, set([door.lower() for door in doors]))
                elif is_door(cell):
                    queue.append((next_pos, dist + 1, doors | {cell}))
                else:
                    queue.append((next_pos, dist + 1, doors))

    return graph


def explore_bfs(vault, robots, goal):
    graph = {}
    for key, pos in goal.items():
        graph[key] = options_bfs(vault, pos)
    for i, start in enumerate(robots):
        graph[str(i)] = options_bfs(vault, start)

    blocked = {}

    visited, queue = set(), [(0, ('0', '1', '2', '3'), set())]
    while queue:
        dist, positions, keys = heapq.heappop(queue)
        # print(dist, positions, keys, len(queue))
        if (positions, tuple(keys)) in visited:
            continue
        visited.add((positions, tuple(keys)))
        if keys == set(goal.keys()):
            return dist
        for i, key in enumerate(positions):
            for next_key, (next_dist, next_pos, doors) in graph[key].items():
                if len(doors - keys) == 0:
                    next_positions = list(positions)
                    next_positions[i] = next_key
                    next_positions = tuple(next_positions)
                    if (next_positions, tuple(keys | {next_key})) not in visited:
                        heapq.heappush(queue, (dist + next_dist, next_positions, keys | {next_key}))
                else:
                    # queue.append((dist, key, keys))
                    pass

    assert False, "didn't find a solution"


def solve(input):
    vault = input.strip().split('\n')
    robots = find_me(vault)
    goal = collect_keys(vault)

    moves = explore_bfs(vault, robots, goal)
    return moves


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
