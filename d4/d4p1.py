from utils.test_case import TestCase

INPUT = '134564-585159'

TEST_CASES = [
    TestCase('111111', 1),
    TestCase('223450', 0),
    TestCase('123789', 0),
]


def check_password(pwd):
    return len(pwd) == 6 and any(d1 == d2 for d1, d2 in zip(pwd[:5], pwd[1:])) and pwd == ''.join(sorted(pwd))


def solve(input):
    min, max = map(int, input.split('-'))
    return sum(check_password(str(pwd)) for pwd in range(min, max + 1))


if __name__ == '__main__':
    for case in TEST_CASES:
        result = check_password(case.case)
        case.check(result)

    print(solve(INPUT))
