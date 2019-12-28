from collections import namedtuple

TestCase = namedtuple('TestCase', 'case expected')

INPUT = """
1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0
"""


def check_case(test_case, actual):
    if test_case.expected == actual:
        print("OK %s" % (test_case.case,))
    else:
        print("FAIL %s, expected %s, got %s" % (test_case.case, test_case.expected, actual))


TEST_CASES = [
    TestCase('1,9,10,3,2,3,11,0,99,30,40,50', 3500),
]

SUM = 1
MUL = 2


def run_program(input, noun=None, verb=None):
    memory = list(map(int, input.strip().split(',')))
    if noun is not None:
        memory[1] = noun
    if verb is not None:
        memory[2] = verb
    pc = 0
    while memory[pc] != 99:
        operation = memory[pc]
        op1 = memory[memory[pc + 1]]
        op2 = memory[memory[pc + 2]]
        res = (op1 + op2) if operation == SUM else (op1 * op2)
        memory[memory[pc + 3]] = res
        pc = pc + 4
    return memory[0]


def solve(input, expected):
    for noun in range(0, 100):
        for verb in range(0, 100):
            actual = run_program(input, noun, verb)
            print(noun, verb, actual)
            if actual == expected:
                return 100 * noun + verb


if __name__ == '__main__':
    for case in TEST_CASES:
        result = run_program(case.case)
        check_case(case, result)

    print(solve(INPUT, 19690720))
