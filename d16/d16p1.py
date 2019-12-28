from utils.test_case import TestCase

INPUT = """
59709511599794439805414014219880358445064269099345553494818286560304063399998657801629526113732466767578373307474609375929817361595469200826872565688108197109235040815426214109531925822745223338550232315662686923864318114370485155264844201080947518854684797571383091421294624331652208294087891792537136754322020911070917298783639755047408644387571604201164859259810557018398847239752708232169701196560341721916475238073458804201344527868552819678854931434638430059601039507016639454054034562680193879342212848230089775870308946301489595646123293699890239353150457214490749319019572887046296522891429720825181513685763060659768372996371503017206185697
"""

TEST_CASES = [
    TestCase("12345678|4", "01029498"),
    TestCase("80871224585914546619083218645595|100", "24176176"),
    TestCase("19617804207202209144916044189917|100", "73745418"),
    TestCase("69317163492948606335995924319873|100", "52432133"),
]

PATTERN = list(map(int, "0, 1, 0, -1".split(', ')))


def element(base_pattern, repeats):
    while True:
        for d in base_pattern:
            for _ in range(repeats):
                yield d


def solve(input, phases):
    lst = list(map(int, list(input)))
    for _ in range(phases):
        next_lst = []
        for i, l in enumerate(range(len(lst))):
            pattern = element(PATTERN, i + 1)
            pattern.__next__()
            o = sum([d*e for d, e in zip(lst, pattern)])
            next_lst.append(abs(o) % 10)
        lst = next_lst

    return ''.join(str(d) for d in lst[:8])


if __name__ == '__main__':
    for case in TEST_CASES:
        input, phases = case.case.split('|')
        result = solve(input, int(phases))
        case.check(result)

    print(solve(INPUT.strip(), 100))
