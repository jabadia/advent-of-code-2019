from utils.test_case import TestCase

INPUT = """
deal with increment 55
cut -6791
deal with increment 9
cut -5412
deal with increment 21
deal into new stack
deal with increment 72
cut -362
deal with increment 24
cut -5369
deal with increment 22
cut 731
deal with increment 72
cut 412
deal into new stack
deal with increment 22
cut -5253
deal with increment 73
deal into new stack
cut -6041
deal into new stack
cut 6605
deal with increment 6
cut 9897
deal with increment 59
cut -9855
deal into new stack
cut -7284
deal with increment 7
cut 332
deal with increment 37
deal into new stack
deal with increment 43
deal into new stack
deal with increment 59
cut 1940
deal with increment 16
cut 3464
deal with increment 24
cut -7766
deal with increment 36
cut -156
deal with increment 18
cut 8207
deal with increment 33
cut -393
deal with increment 4
deal into new stack
cut -4002
deal into new stack
cut -8343
deal into new stack
deal with increment 70
deal into new stack
cut 995
deal with increment 22
cut 1267
deal with increment 47
cut -3161
deal into new stack
deal with increment 34
cut -6221
deal with increment 26
cut 4956
deal with increment 57
deal into new stack
cut -4983
deal with increment 36
cut -1101
deal into new stack
deal with increment 2
cut 4225
deal with increment 35
cut -721
deal with increment 17
cut 5866
deal with increment 40
cut -531
deal into new stack
deal with increment 63
cut -5839
deal with increment 30
cut 5812
deal with increment 35
deal into new stack
deal with increment 46
cut -5638
deal with increment 60
deal into new stack
deal with increment 33
cut -4690
deal with increment 7
cut 6264
deal into new stack
cut 8949
deal into new stack
cut -4329
deal with increment 52
cut 3461
deal with increment 47
"""

TEST_CASES = [
    TestCase("deal into new stack", "10 9 8 7 6 5 4 3 2 1 0"),
    TestCase("cut -4", "7 8 9 10 0 1 2 3 4 5 6"),
    TestCase("cut 3", "3 4 5 6 7 8 9 10 0 1 2"),
    # TestCase("deal with increment 3", "0 7 4 1 8 5 2 9 6 3"),
    # TestCase("deal with increment 7", "0 3 6 9 2 5 8 1 4 7"),
    # TestCase("deal with increment 9", "0 9 8 7 6 5 4 3 2 1"),
    TestCase("deal with increment 3", "0 4 8 1 5 9 2 6 10 3 7"),
    TestCase("deal with increment 7", "0 8 5 2 10 7 4 1 9 6 3"),
    TestCase("deal with increment 9", "0 5 10 4 9 3 8 2 7 1 6"),
    TestCase("""
deal with increment 7
deal into new stack
deal into new stack""", "0 3 6 9 2 5 8 1 4 7"),
    TestCase("""
cut 6
deal with increment 7
deal into new stack""", "3 0 7 4 1 8 5 2 9 6"),
    TestCase("""
deal with increment 7
deal with increment 9
cut -2""", "6 3 0 7 4 1 8 5 2 9"),
    TestCase("""
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1""", "9 2 5 8 1 4 7 0 3 6"),
]


def rev_deal_with_increment(N, i, deck):
    return i * pow(N, deck-2, deck) % deck
# 3, 1, 10 -> 7
# 3, 2, 10 -> 4
# 3, 3, 10 -> 1
# 9, 1, 10 -> 9
# 9, 2, 10 -> 8
# 9, 3, 10 -> 7


def rev_cut(N, i, deck):
    return (i + N) % deck


def rev_deal_into_new_stack(i, deck):
    return deck - i - 1


# DECK = 10007
DECK = 119315717514047
TIMES = 101741582076661


def run_sequence(sequence, i, deck):
    for line in reversed(sequence.strip().split('\n')):
        if line.startswith('deal with increment'):
            N = int(line.split(' ')[-1])
            i = rev_deal_with_increment(N, i, deck)
        elif line.startswith('deal into new stack'):
            i = rev_deal_into_new_stack(i, deck)
        elif line.startswith('cut'):
            N = int(line.split(' ')[-1])
            i = rev_cut(N, i, deck)

    return i


def solve(sequence, test=False):
    deck = 11 if test else DECK

    if test:
        result = ' '.join([str(run_sequence(sequence, i, deck)) for i in range(deck)])
    else:
        i = 0
        result = 2020
        partials = {}
        while True:
            result = run_sequence(sequence, result, deck)
            if result == 2020:
                return partials[TIMES % i]
            partials[i] = result
            i += 1
            if i % 10000 == 0:
                print(i)


    return result


if __name__ == '__main__':
    for case in TEST_CASES[:6]:
        result = solve(case.case, test=True)
        case.check(result)

    print(solve(INPUT))
