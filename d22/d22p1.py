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
    TestCase("deal into new stack", "9 8 7 6 5 4 3 2 1 0"),
    TestCase("cut -4", "6 7 8 9 0 1 2 3 4 5"),
    TestCase("cut 3", "3 4 5 6 7 8 9 0 1 2"),
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


def deal_with_increment(N, deck):
    L = len(deck)
    new_deck = [None] * L
    i = 0
    for j in range(L):
        new_deck[i] = deck[j]
        i = (i + N) % L
    return new_deck


def cut(N, deck):
    return deck[N:] + deck[:N]


def deal_into_new_stack(deck):
    return list(reversed(deck))


def solve(sequence, test=False):
    deck = list(range(10 if test else 10007))
    for line in sequence.strip().split('\n'):
        if line.startswith('deal with increment'):
            N = int(line.split(' ')[-1])
            deck = deal_with_increment(N, deck)
        elif line.startswith('deal into new stack'):
            deck = deal_into_new_stack(deck)
        elif line.startswith('cut'):
            N = int(line.split(' ')[-1])
            deck = cut(N, deck)

    if test:
        return ' '.join([str(n) for n in deck])
    else:
        return deck.index(2019)


if __name__ == '__main__':
    # for case in TEST_CASES:
    #     result = solve(case.case, test=True)
    #     case.check(result)

    print(3, '||', ' '.join([str(n) for n in deal_with_increment(3, list(range(11)))]))
    print(7, '||', ' '.join([str(n) for n in deal_with_increment(7, list(range(11)))]))
    print(9, '||', ' '.join([str(n) for n in deal_with_increment(9, list(range(11)))]))

    print(solve(INPUT))
