from collections import namedtuple

TestCase = namedtuple('TestCase', 'case expected')

INPUT = """
50951
69212
119076
124303
95335
65069
109778
113786
124821
103423
128775
111918
138158
141455
92800
50908
107279
77352
129442
60097
84670
143682
104335
105729
87948
59542
81481
147508
62687
64212
66794
99506
137804
135065
135748
110879
114412
120414
72723
50412
124079
57885
95601
74974
69000
66567
118274
136432
110395
88893
124962
74296
106148
59764
123059
106473
50725
116256
80314
60965
134002
53389
82528
144323
87791
128288
109929
64373
114510
116897
84697
75358
109246
110681
94543
92590
69865
83912
124275
94276
98210
69752
100315
142879
94783
111939
64170
83629
138743
141238
77068
119299
81095
96515
126853
87563
101299
130240
62693
139018
"""


def check_case(test_case, actual):
    if test_case.expected == actual:
        print("OK %s" % (test_case.case,))
    else:
        print("FAIL %s, expected %s, got %s" % (test_case.case, test_case.expected, actual))


TEST_CASES = [
    TestCase('14', 2),
    TestCase('1969', 966),
    TestCase('100756', 50346),
]


def fuel(mass):
    required_fuel = max(0, mass // 3 - 2)
    return required_fuel + (fuel(required_fuel) if required_fuel > 0 else 0)


def solve(input):
    masses = input.strip().split('\n')
    return sum(fuel(int(mass)) for mass in masses)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        check_case(case, result)

    print(solve(INPUT))
