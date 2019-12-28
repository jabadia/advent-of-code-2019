from utils.test_case import TestCase
from utils.intcode import Intcode

INPUT = """
3,8,1005,8,310,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,29,1,2,11,10,1,1101,2,10,2,1008,18,10,2,106,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,67,2,105,15,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,93,2,1001,16,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,119,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,141,2,7,17,10,1,1103,16,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,170,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,193,1,7,15,10,2,105,13,10,1006,0,92,1006,0,99,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,228,1,3,11,10,1006,0,14,1006,0,71,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,261,2,2,2,10,1006,0,4,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,289,101,1,9,9,1007,9,1049,10,1005,10,15,99,109,632,104,0,104,1,21101,0,387240009756,1,21101,327,0,0,1105,1,431,21101,0,387239486208,1,21102,1,338,0,1106,0,431,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,3224472579,1,1,21101,0,385,0,1106,0,431,21101,0,206253952003,1,21102,396,1,0,1105,1,431,3,10,104,0,104,0,3,10,104,0,104,0,21102,709052072296,1,1,21102,419,1,0,1105,1,431,21102,1,709051962212,1,21102,430,1,0,1106,0,431,99,109,2,21202,-1,1,1,21102,1,40,2,21102,462,1,3,21102,452,1,0,1105,1,495,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,457,458,473,4,0,1001,457,1,457,108,4,457,10,1006,10,489,1101,0,0,457,109,-2,2105,1,0,0,109,4,2102,1,-1,494,1207,-3,0,10,1006,10,512,21101,0,0,-3,22101,0,-3,1,21202,-2,1,2,21102,1,1,3,21101,531,0,0,1105,1,536,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,559,2207,-4,-2,10,1006,10,559,21202,-4,1,-4,1105,1,627,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,578,0,1105,1,536,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,597,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,619,21201,-1,0,1,21102,1,619,0,106,0,494,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0
"""

TEST_CASES = [
    TestCase("(1,0),(0,0),(1,0),(1,0),(0,1),(1,0),(1,0)", 6),
]


class MockRobot(object):
    def __init__(self, outputs):
        pairs = outputs[1:-1].split('),(')
        self.outputs = [o for pair in pairs for o in pair.split(',')]

    def run(self, input):
        if len(self.outputs) == 0:
            return 'END'
        next = self.outputs.pop(0)
        return next


def move(robot):
    if robot[2] == '^':
        return robot[0], robot[1] + 1, robot[2]
    elif robot[2] == 'v':
        return robot[0], robot[1] - 1, robot[2]
    elif robot[2] == '<':
        return robot[0] - 1, robot[1], robot[2]
    elif robot[2] == '>':
        return robot[0] + 1, robot[1], robot[2]
    else:
        assert False, "bad direction"


LEFT = '0'
RIGHT = '1'

BLACK = '0'
WHITE = '1'

DIRECTIONS = ['^', '>', 'v', '<']


def turn(robot, side):
    return (
        robot[0],
        robot[1],
        DIRECTIONS[(DIRECTIONS.index(robot[2]) + (1 if side == RIGHT else -1)) % len(DIRECTIONS)]
    )


assert turn((0, 0, '^'), LEFT) == (0, 0, '<')
assert turn((0, 0, '<'), LEFT) == (0, 0, 'v')
assert turn((0, 0, 'v'), LEFT) == (0, 0, '>')
assert turn((0, 0, '>'), LEFT) == (0, 0, '^')

assert turn((0, 0, '<'), RIGHT) == (0, 0, '^')
assert turn((0, 0, 'v'), RIGHT) == (0, 0, '<')
assert turn((0, 0, '>'), RIGHT) == (0, 0, 'v')
assert turn((0, 0, '^'), RIGHT) == (0, 0, '>')


def print_world(panels, robot):
    minx = min(coord[0] for coord in panels)
    maxx = max(coord[0] for coord in panels)
    miny = min(coord[1] for coord in panels)
    maxy = max(coord[1] for coord in panels)
    for y in range(maxy, miny - 1, -1):
        for x in range(minx, maxx + 1):
            if robot[0] == x and robot[1] == y:
                print(robot[2], end='')
            else:
                color = panels.get((x, y), BLACK)
                print('##' if color == WHITE else '  ', end='')
        print()
    print()


def solve(program):
    robot_brain = MockRobot(program) if '(' in program else Intcode(program)
    robot = (0, 0, '^')
    panels = {}
    while True:
        color = panels.get((robot[0], robot[1]), WHITE)
        paint, side = robot_brain.run(color), robot_brain.run(color)
        if paint == 'END':
            return len(panels)
        panels[(robot[0], robot[1])] = paint
        robot = move(turn(robot, side))
        print(len(panels))
        print_world(panels, robot)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
