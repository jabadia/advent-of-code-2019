from utils.test_case import TestCase

# hint: https://topaz.github.io/paste/#XQAAAQCcCwAAAAAAAAA0m0pnuFI8c+fPp4HB1KdZ5eFWD1VYmJWe9xkvfbjYYzCdzzWruPBbteW/ueKh1tReLlkGjRZ9zyj1Hlyjuz0s8UgMbdm1avNXj6I7EM0ERFKgPrHpgM3fxd6GWRB8RxbX8FVfy9vbamhqtKpsES89SV4Vou5EVqpd5Brym3pX5SHX1TuLdkr2MZ1CVUPiA5hM2c+PFHm5+pCkI+kVmzauNXcjo87BOu6vTLTYHp4sHfQ/h0e3BSFJ9Cnw4aIrQZLhF8ms0EMGeA7gCpdChCA5bVGOjnVCvKlPuu8odniL3CMruE/aN+GmaKKLwrXXpeP9BYlslWN/O8rVD+GObmLSIItA4V3YFjZHbii4KLvw723/PpXFU3PtrzfobGKmXiTCMublHjyl3gUXxQPI1lvSr1YRbFlawz7hW4YlLho0z4Wj27u+D9invu73qjn0BBnXJL/7SKMYcum2UFtFqhXia/MzL75Oxb59j/tVsndWBQc720B+9Ee7aZgmetF68cwQ9OQZF7Aj8PkEki/w/k2HJqIfyX5t8P+IdknwgShdoAm8oFw57oz5/Z1dVCxrah0Ach88TWQZR4u4CdgiZNQ9uOmBWnM+Dv5pODvm6qkaIb30pMwV65yRcehIuWKKq3GC0drAfnecjszExv8eujPWCxDDWyqOLVmE+FRw5FJSzqVJe/Gah7ov5BWjqigsDbuoLD+fXnIqxuIRZNoovsVYtFiuClZIIvNXUvwnsCYblAmzShkhAxpqNgK76BSfCdq+/8ke0vluIbYEJKgSMHJUL0za6NyuS33UMCxTsyp1/hQtXoX9a+RoposKOGAYGqb2b07Fbxpmenv84fPv9MFjXCOp2D7WRKh6nbs5Pk+M9b9u26rJHT8TPq9384bak9I3hdtJtWj/qsrmxMOCEYX1CHwBEcCOqXKfg54KOn7xhNT2pOOLpe2W6ctScxShwvMr80sAxjP7lpyn51ER0PMSCHv3PIoq8YLt7A1QaGqshTtEEVV8JOmIXxywxiAhmzR/Ku5QNLLfyNYrKioJpqcMgTcy7SHspR0ZHMJ6q8P2bIJ6WkytnaWdTXcnXgtqxbFgwhNr6Mm42ICJFgX7uoKpEGmZV9CPoDQMXQZgJsZ/MElLUJWBDAaZme9jMOef/tnTRcfCSpMfN4x/dG5g9eybAikLIg0+N60FSyJmwI5Gnahbdr7K1ULX8NcyHW1WGagp57kyGibiKI+TTzPwyUTzkO883+8B6TE0b7h9hbVWOLvA3X7IUJhh96cvrgWl6tLjnI60nJt1FnM8seoTOaU4NMyjOt51smYVR0abNA+NNSLDJC3Ghqx7k9x5z09t6EV/3cTZbCgKI8GRRELdkA1bGDjwekFGk4ugvUm3qhE3KJ0tJoAx4m+X5IzDbWIIbyuhTH1IHC6GtdX2JD+NVb6YUI0eRGnpP/liI/areI8lr0hwCd3Frn8i/oJQnfQZv14+ajkonea1KrnIx9oopNvKsG9IhrFrP8WWZ2n4BFT7zP3MyXqOMeq3/0CwYUv2B8zbHIZUWNQxgyO3Vpkbkfh8VFKWFaFSscLDTHBw2BTJ7DQ4bC3aY//gS4e7

# another solution

# from itertools import cycle, accumulate
# def level2():
#     with open("data/day16.txt") as f:
#         s = f.read().strip()
#     offset = int(s[:7])
#     digits = [int(i) for i in s]
#     # If `rep` is `digits` repeated 10K times, construct:
#     #     arr = [rep[-1], rep[-2], ..., rep[offset]]
#     l = 10000 * len(digits) - offset
#     i = cycle(reversed(digits))
#     arr = [next(i) for _ in range(l)]
#     # Repeatedly take the partial sums mod 10
#     for _ in range(100):
#         arr = [n % 10 for n in accumulate(arr)]
#     return "".join(str(i) for i in arr[-1:-9:-1])

INPUT = """
59709511599794439805414014219880358445064269099345553494818286560304063399998657801629526113732466767578373307474609375929817361595469200826872565688108197109235040815426214109531925822745223338550232315662686923864318114370485155264844201080947518854684797571383091421294624331652208294087891792537136754322020911070917298783639755047408644387571604201164859259810557018398847239752708232169701196560341721916475238073458804201344527868552819678854931434638430059601039507016639454054034562680193879342212848230089775870308946301489595646123293699890239353150457214490749319019572887046296522891429720825181513685763060659768372996371503017206185697
"""

TEST_CASES = [
    TestCase("03036732577212944063491565474664|100", "84462026"),
    TestCase("02935109699940807407585447034323|100", "78725270"),
    TestCase("03081770884921959731165446850517|100", "53553731"),
]

PATTERN = list(map(int, "0, 1, 0, -1".split(', ')))


def element(base_pattern, repeats):
    while True:
        for d in base_pattern:
            for _ in range(repeats):
                yield d


def solve(input, phases):
    offset = int(input[:7])
    lst = list(map(int, list(input)))
    for _ in range(phases):
        next_lst = []
        for i, l in enumerate(range(len(lst))):
            pattern = element(PATTERN, i + 1)
            pattern.__next__()
            o = sum([d*e for d, e in zip(lst, pattern)])
            next_lst.append(abs(o) % 10)
        lst = next_lst

    return ''.join(str(d) for d in lst)


if __name__ == '__main__':
    for case in TEST_CASES:
        input, phases = case.case.split('|')
        result = solve(input, int(phases))
        case.check(result)

    print(solve(INPUT.strip(), 100))
