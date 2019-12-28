from collections import defaultdict
from math import atan2

from utils.test_case import TestCase

INPUT = """
15 RNMTG => 6 QSXV
21 MKJN => 9 KDFZ
1 KVFL, 4 NZWL => 3 FHDT
1 FZJXD, 2 SWZK, 1 QRLRS => 6 ZRNK
8 KVFL => 6 SBZKF
11 DXFB, 1 CPBXJ, 8 TXFCS, 1 ZPMHL, 1 BCHTD, 2 FZJXD, 2 WKZMQ, 1 NZWL => 8 MPLJ
5 KDFZ, 1 QSXV => 9 TXFCS
1 PMLGM, 21 CKVN => 3 KVFL
1 XFRLH, 3 QRLRS => 4 CKVN
5 KBJS, 15 XFRLH, 6 WZPZX, 15 KVFL, 4 DXFB, 4 ZPMHL, 11 JCKCK, 26 KFGPB => 9 BWVS
10 KNRDW, 2 XCML => 9 BCNL
26 LBLH => 9 KBJS
5 DTFBQ, 4 PJTD => 6 FHKSW
6 HTRFP, 1 FVXV, 4 JKLNF, 1 TXFCS, 2 PXBP => 4 JRBFT
21 DTFBQ => 9 JGQJ
2 KBJS => 3 FZJXD
24 LBLH => 6 QFMTZ
1 CBNJT => 7 LSCW
5 KVFL => 2 NZWL
12 DNHL, 4 BCNL => 4 LBLH
15 RHVG => 1 PJCWT
4 KDFZ, 1 KVFL => 3 BCHTD
2 XFDW, 7 BCHTD => 7 WKZMQ
2 SBZKF, 1 PLTX => 3 DXFB
1 PLTX, 11 HTRFP, 6 PMLGM => 1 JCKCK
1 TQCX, 10 DNHL => 8 DTFBQ
2 TQCX, 2 KTBFB => 5 RHVG
8 MVFW => 3 CPBXJ
148 ORE => 4 CBNJT
9 CPBXJ, 5 DTFBQ => 6 PMLGM
11 ZXCF, 15 PJCWT, 4 FZJXD => 7 PJTD
1 JGQJ => 6 DCBNV
4 LSCW, 16 BCNL => 7 MVFW
1 RHVG => 4 XFDW
8 MPLJ, 16 JRBFT, 43 KBJS, 11 NZWL, 4 BWVS, 22 ZPMHL => 1 FUEL
1 QFMTZ, 3 CKVN => 5 PLTX
5 CKVN, 10 SWZK => 7 HTRFP
2 PXBP, 1 QRLRS, 7 KTBFB => 7 NDZGV
1 QRLRS, 9 KBJS, 2 TQCX => 2 SWZK
9 TZKZ, 3 ZRNK, 4 PXBP => 4 FVXV
1 PMLGM, 1 SWZK, 6 FZJXD => 7 MKJN
16 MVFW, 2 KBJS => 7 ZXCF
1 MVFW => 6 HVGF
1 LSCW, 1 HVGF => 8 RNMTG
5 ZRNK, 1 TQCX => 3 PXBP
130 ORE => 5 KNRDW
1 RHVG, 2 KFGPB, 1 LSCW => 7 QRLRS
6 XFRLH => 8 TZKZ
24 HVGF, 8 KTBFB => 1 XFRLH
2 KNRDW, 2 CBNJT => 6 DNHL
1 FHDT => 4 JKLNF
1 QSXV, 10 XFGZX, 2 DCBNV => 8 ZPMHL
1 FHDT, 7 NDZGV => 4 WZPZX
11 FHKSW => 5 XFGZX
10 LSCW => 8 KTBFB
133 ORE => 1 XCML
8 XCML => 4 TQCX
6 CPBXJ, 8 CBNJT => 6 KFGPB
"""

TEST_CASES = [
    TestCase("""
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
""", 82892753),
    TestCase("""
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
""", 5586022),
    TestCase("""
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
""", 460664)
]

INPUTS = 1
OUTPUT = 0

QUANTITY = 0
ELEMENT = 1


def exdiv(a, b):
    return (a + b - 1) // b


def solve(input):
    reaction_lines = [line.split(' => ') for line in input.strip().split('\n')]
    reactions = {}
    for reaction_inputs, reaction_output in reaction_lines:
        reaction_inputs = [reaction_input.split(' ') for reaction_input in reaction_inputs.split(', ')]
        reaction_inputs = [(int(quantity), element) for quantity, element in reaction_inputs]
        reaction_output = reaction_output.split(' ')
        reaction_output = int(reaction_output[0]), reaction_output[1]
        assert reaction_output[1] not in reactions
        reactions[reaction_output[1]] = (reaction_output, reaction_inputs)

    # for element, reaction in reactions.items():
    #     print(reaction)

    assert reactions['FUEL'][OUTPUT][QUANTITY] == 1
    # needed_ingredients = defaultdict(int, {element: quantity for quantity, element in reactions['FUEL'][INPUTS]})
    # waste_ingredients = defaultdict(int)
    # ore_needs = 0
    # while needed_ingredients:
    #     # print(needed_ingredients)
    #     element, quantity = needed_ingredients.popitem()
    #     if waste_ingredients[element]:
    #         used = min(waste_ingredients[element], quantity)
    #         quantity -= used
    #         waste_ingredients[element] -= used
    #     if quantity == 0:
    #         continue
    #     reaction = reactions[element]
    #     times = exdiv(quantity, reaction[OUTPUT][QUANTITY])
    #     for input in reaction[INPUTS]:
    #         if input[ELEMENT] == 'ORE':
    #             ore_needs += times * input[QUANTITY]
    #         else:
    #             needed_ingredients[input[ELEMENT]] += times * input[QUANTITY]
    #     waste_ingredients[element] += (times * reaction[OUTPUT][QUANTITY]) - quantity

    ore_remaining = 1_000_000_000_000
    fuel_produced = 0
    waste_ingredients = defaultdict(int)
    seen_waste = {}
    while True:
        needed_ingredients = defaultdict(int, {element: quantity for quantity, element in reactions['FUEL'][INPUTS]})
        while needed_ingredients:
            # print(needed_ingredients)
            element, quantity = needed_ingredients.popitem()
            if waste_ingredients[element]:
                used = min(waste_ingredients[element], quantity)
                quantity -= used
                waste_ingredients[element] -= used
            if quantity == 0:
                continue
            reaction = reactions[element]
            times = exdiv(quantity, reaction[OUTPUT][QUANTITY])
            for input in reaction[INPUTS]:
                if input[ELEMENT] == 'ORE':
                    if ore_remaining >= times * input[QUANTITY]:
                        ore_remaining -= times * input[QUANTITY]
                    else:
                        return fuel_produced
                else:
                    needed_ingredients[input[ELEMENT]] += times * input[QUANTITY]
            waste_ingredients[element] += (times * reaction[OUTPUT][QUANTITY]) - quantity

        fuel_produced += 1
        waste = tuple(waste_ingredients.items())
        if waste in seen_waste:
            start_ore_consumed, start_fuel_produced = seen_waste[waste]
            ore_consumed = 1_000_000_000_000 - ore_remaining - start_ore_consumed
            print(seen_waste[waste], fuel_produced, ore_consumed)
            cycles = ore_remaining // ore_consumed
            fuel_produced += cycles * (fuel_produced - start_fuel_produced)
            ore_remaining -= cycles * ore_consumed
            seen_waste = {}
        else:
            seen_waste[waste] = (1_000_000_000_000 - ore_remaining, fuel_produced)
        # if fuel_produced % 100000 == 0:
        #     print(fuel_produced, ore_remaining, waste_ingredients)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
