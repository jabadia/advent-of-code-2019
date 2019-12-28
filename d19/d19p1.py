from utils.test_case import TestCase
from utils.intcode import Intcode

INPUT = """
109,424,203,1,21101,11,0,0,1105,1,282,21102,1,18,0,1105,1,259,2102,1,1,221,203,1,21102,1,31,0,1105,1,282,21102,38,1,0,1105,1,259,20101,0,23,2,22102,1,1,3,21101,1,0,1,21101,57,0,0,1105,1,303,2101,0,1,222,21002,221,1,3,21002,221,1,2,21102,1,259,1,21101,0,80,0,1105,1,225,21102,83,1,2,21102,1,91,0,1106,0,303,2101,0,1,223,20102,1,222,4,21101,0,259,3,21101,0,225,2,21101,225,0,1,21101,118,0,0,1106,0,225,20101,0,222,3,21101,34,0,2,21101,133,0,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,1201,1,0,223,20102,1,221,4,20101,0,222,3,21101,12,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,108,20207,1,223,2,20101,0,23,1,21102,1,-1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22101,0,-3,1,22101,0,-2,2,21201,-1,0,3,21101,0,250,0,1105,1,225,21201,1,0,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,343,0,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21101,384,0,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0
"""

TEST_CASES = [
    # TestCase("""""", 76),
]

N = 50


def print_map(area):
    for y in range(N):
        for x in range(N):
            print('#' if area[(x, y)] == '1' else '.', end='')
        print()


def solve(program):
    area = {}
    count = 0
    for y in range(N):
        for x in range(N):
            intcode = Intcode(program)
            beam = intcode.run([x, y])
            if beam == '1':
                count += 1
            area[(x, y)] = beam

    print_map(area)
    return count


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
