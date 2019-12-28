from utils.test_case import TestCase

INPUT = '134564-585159'

TEST_CASES = [
    TestCase('111111', False),
    TestCase('223450', False),
    TestCase('123789', False),
    TestCase('112233', True),
    TestCase('112233', True),
    TestCase('123444', False),
    TestCase('111122', True),
]


def check_password(pwd):
    repeat_count, last_c = 0, ''
    for c in pwd:
        if c == last_c:
            repeat_count += 1
        else:
            if repeat_count == 1:
                break
            repeat_count = 0
        last_c = c
    has_pair = repeat_count == 1
    return len(pwd) == 6 and has_pair and pwd == ''.join(sorted(pwd))


def solve(input):
    min, max = map(int, input.split('-'))
    return sum(check_password(str(pwd)) for pwd in range(min, max + 1))


if __name__ == '__main__':
    for case in TEST_CASES:
        result = check_password(case.case)
        case.check(result)

    print(solve(INPUT))
