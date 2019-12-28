from utils.test_case import TestCase
from utils.intcode import Intcode

INPUT = """
109,2050,21102,966,1,1,21102,1,13,0,1106,0,1378,21102,1,20,0,1105,1,1337,21101,0,27,0,1106,0,1279,1208,1,65,748,1005,748,73,1208,1,79,748,1005,748,110,1208,1,78,748,1005,748,132,1208,1,87,748,1005,748,169,1208,1,82,748,1005,748,239,21102,1041,1,1,21101,0,73,0,1106,0,1421,21102,78,1,1,21101,0,1041,2,21101,0,88,0,1106,0,1301,21102,1,68,1,21101,0,1041,2,21102,1,103,0,1106,0,1301,1101,1,0,750,1106,0,298,21101,0,82,1,21102,1041,1,2,21102,1,125,0,1105,1,1301,1102,1,2,750,1105,1,298,21102,1,79,1,21102,1041,1,2,21101,0,147,0,1105,1,1301,21102,84,1,1,21101,0,1041,2,21101,0,162,0,1106,0,1301,1102,3,1,750,1105,1,298,21101,0,65,1,21101,1041,0,2,21101,184,0,0,1106,0,1301,21101,76,0,1,21102,1041,1,2,21102,199,1,0,1105,1,1301,21102,1,75,1,21101,1041,0,2,21101,214,0,0,1105,1,1301,21101,0,221,0,1105,1,1337,21101,0,10,1,21102,1,1041,2,21102,236,1,0,1105,1,1301,1106,0,553,21102,85,1,1,21101,0,1041,2,21102,254,1,0,1106,0,1301,21101,0,78,1,21101,1041,0,2,21102,269,1,0,1105,1,1301,21101,0,276,0,1106,0,1337,21101,10,0,1,21102,1041,1,2,21101,0,291,0,1106,0,1301,1102,1,1,755,1106,0,553,21102,1,32,1,21102,1,1041,2,21102,313,1,0,1106,0,1301,21101,320,0,0,1105,1,1337,21101,327,0,0,1105,1,1279,1202,1,1,749,21101,0,65,2,21102,1,73,3,21101,0,346,0,1105,1,1889,1206,1,367,1007,749,69,748,1005,748,360,1102,1,1,756,1001,749,-64,751,1105,1,406,1008,749,74,748,1006,748,381,1102,-1,1,751,1106,0,406,1008,749,84,748,1006,748,395,1101,0,-2,751,1105,1,406,21102,1,1100,1,21101,0,406,0,1105,1,1421,21102,32,1,1,21102,1100,1,2,21101,421,0,0,1105,1,1301,21101,428,0,0,1106,0,1337,21101,0,435,0,1105,1,1279,2101,0,1,749,1008,749,74,748,1006,748,453,1102,1,-1,752,1105,1,478,1008,749,84,748,1006,748,467,1102,-2,1,752,1105,1,478,21101,1168,0,1,21101,0,478,0,1106,0,1421,21101,485,0,0,1106,0,1337,21101,10,0,1,21101,0,1168,2,21101,500,0,0,1105,1,1301,1007,920,15,748,1005,748,518,21101,1209,0,1,21102,518,1,0,1105,1,1421,1002,920,3,529,1001,529,921,529,101,0,750,0,1001,529,1,537,1002,751,1,0,1001,537,1,545,102,1,752,0,1001,920,1,920,1105,1,13,1005,755,577,1006,756,570,21102,1100,1,1,21101,0,570,0,1106,0,1421,21101,987,0,1,1106,0,581,21102,1,1001,1,21102,588,1,0,1105,1,1378,1102,1,758,593,1001,0,0,753,1006,753,654,20101,0,753,1,21102,1,610,0,1106,0,667,21102,0,1,1,21102,621,1,0,1105,1,1463,1205,1,647,21101,1015,0,1,21101,0,635,0,1105,1,1378,21101,1,0,1,21102,646,1,0,1106,0,1463,99,1001,593,1,593,1105,1,592,1006,755,664,1102,0,1,755,1106,0,647,4,754,99,109,2,1101,0,726,757,22101,0,-1,1,21102,1,9,2,21101,697,0,3,21101,0,692,0,1106,0,1913,109,-2,2106,0,0,109,2,1002,757,1,706,1201,-1,0,0,1001,757,1,757,109,-2,2105,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,255,63,95,223,191,159,127,0,250,181,85,214,251,46,216,115,108,172,141,43,227,179,185,126,153,155,58,93,57,173,34,190,49,118,113,70,50,162,187,111,246,62,86,239,42,237,152,201,139,217,233,38,234,219,55,183,226,199,98,109,114,76,229,103,136,231,189,60,244,79,51,221,171,213,39,242,243,232,167,186,236,228,249,54,188,238,142,47,163,204,157,248,122,254,154,119,69,116,253,84,207,200,102,78,170,123,247,203,56,117,71,245,94,77,198,100,137,61,156,177,35,125,182,235,175,205,68,110,107,212,241,202,158,220,121,178,252,206,174,143,169,87,92,230,196,106,218,215,99,101,184,197,138,166,124,59,120,140,53,222,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,73,110,112,117,116,32,105,110,115,116,114,117,99,116,105,111,110,115,58,10,13,10,87,97,108,107,105,110,103,46,46,46,10,10,13,10,82,117,110,110,105,110,103,46,46,46,10,10,25,10,68,105,100,110,39,116,32,109,97,107,101,32,105,116,32,97,99,114,111,115,115,58,10,10,58,73,110,118,97,108,105,100,32,111,112,101,114,97,116,105,111,110,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,78,68,44,32,79,82,44,32,111,114,32,78,79,84,67,73,110,118,97,108,105,100,32,102,105,114,115,116,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,44,32,66,44,32,67,44,32,68,44,32,74,44,32,111,114,32,84,40,73,110,118,97,108,105,100,32,115,101,99,111,110,100,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,74,32,111,114,32,84,52,79,117,116,32,111,102,32,109,101,109,111,114,121,59,32,97,116,32,109,111,115,116,32,49,53,32,105,110,115,116,114,117,99,116,105,111,110,115,32,99,97,110,32,98,101,32,115,116,111,114,101,100,0,109,1,1005,1262,1270,3,1262,21001,1262,0,0,109,-1,2105,1,0,109,1,21101,0,1288,0,1105,1,1263,20102,1,1262,0,1102,0,1,1262,109,-1,2106,0,0,109,5,21101,1310,0,0,1106,0,1279,21202,1,1,-2,22208,-2,-4,-1,1205,-1,1332,22101,0,-3,1,21102,1,1332,0,1106,0,1421,109,-5,2106,0,0,109,2,21102,1,1346,0,1105,1,1263,21208,1,32,-1,1205,-1,1363,21208,1,9,-1,1205,-1,1363,1105,1,1373,21101,0,1370,0,1106,0,1279,1106,0,1339,109,-2,2105,1,0,109,5,1202,-4,1,1386,20102,1,0,-2,22101,1,-4,-4,21102,0,1,-3,22208,-3,-2,-1,1205,-1,1416,2201,-4,-3,1408,4,0,21201,-3,1,-3,1105,1,1396,109,-5,2106,0,0,109,2,104,10,21202,-1,1,1,21101,1436,0,0,1105,1,1378,104,10,99,109,-2,2105,1,0,109,3,20002,593,753,-1,22202,-1,-2,-1,201,-1,754,754,109,-3,2105,1,0,109,10,21101,5,0,-5,21102,1,1,-4,21101,0,0,-3,1206,-9,1555,21101,3,0,-6,21101,0,5,-7,22208,-7,-5,-8,1206,-8,1507,22208,-6,-4,-8,1206,-8,1507,104,64,1105,1,1529,1205,-6,1527,1201,-7,716,1515,21002,0,-11,-8,21201,-8,46,-8,204,-8,1105,1,1529,104,46,21201,-7,1,-7,21207,-7,22,-8,1205,-8,1488,104,10,21201,-6,-1,-6,21207,-6,0,-8,1206,-8,1484,104,10,21207,-4,1,-8,1206,-8,1569,21102,0,1,-9,1106,0,1689,21208,-5,21,-8,1206,-8,1583,21101,0,1,-9,1105,1,1689,1201,-5,716,1589,20101,0,0,-2,21208,-4,1,-1,22202,-2,-1,-1,1205,-2,1613,21202,-5,1,1,21101,1613,0,0,1105,1,1444,1206,-1,1634,22102,1,-5,1,21101,1627,0,0,1105,1,1694,1206,1,1634,21101,2,0,-3,22107,1,-4,-8,22201,-1,-8,-8,1206,-8,1649,21201,-5,1,-5,1206,-3,1663,21201,-3,-1,-3,21201,-4,1,-4,1106,0,1667,21201,-4,-1,-4,21208,-4,0,-1,1201,-5,716,1676,22002,0,-1,-1,1206,-1,1686,21102,1,1,-4,1106,0,1477,109,-10,2105,1,0,109,11,21101,0,0,-6,21101,0,0,-8,21102,1,0,-7,20208,-6,920,-9,1205,-9,1880,21202,-6,3,-9,1201,-9,921,1724,21001,0,0,-5,1001,1724,1,1732,21001,0,0,-4,22102,1,-4,1,21102,1,1,2,21102,1,9,3,21102,1,1754,0,1106,0,1889,1206,1,1772,2201,-10,-4,1766,1001,1766,716,1766,21002,0,1,-3,1105,1,1790,21208,-4,-1,-9,1206,-9,1786,22101,0,-8,-3,1106,0,1790,22101,0,-7,-3,1001,1732,1,1795,21001,0,0,-2,21208,-2,-1,-9,1206,-9,1812,21202,-8,1,-1,1106,0,1816,21202,-7,1,-1,21208,-5,1,-9,1205,-9,1837,21208,-5,2,-9,1205,-9,1844,21208,-3,0,-1,1106,0,1855,22202,-3,-1,-1,1105,1,1855,22201,-3,-1,-1,22107,0,-1,-1,1105,1,1855,21208,-2,-1,-9,1206,-9,1869,22101,0,-1,-8,1105,1,1873,22102,1,-1,-7,21201,-6,1,-6,1105,1,1708,22102,1,-8,-10,109,-11,2105,1,0,109,7,22207,-6,-5,-3,22207,-4,-6,-2,22201,-3,-2,-1,21208,-1,0,-6,109,-7,2106,0,0,0,109,5,2101,0,-2,1912,21207,-4,0,-1,1206,-1,1930,21101,0,0,-4,22101,0,-4,1,21202,-3,1,2,21102,1,1,3,21102,1949,1,0,1105,1,1954,109,-5,2105,1,0,109,6,21207,-4,1,-1,1206,-1,1977,22207,-5,-3,-1,1206,-1,1977,21201,-5,0,-5,1106,0,2045,21201,-5,0,1,21201,-4,-1,2,21202,-3,2,3,21101,1996,0,0,1105,1,1954,21202,1,1,-5,21101,1,0,-2,22207,-5,-3,-1,1206,-1,2015,21101,0,0,-2,22202,-3,-2,-3,22107,0,-4,-1,1206,-1,2037,22102,1,-2,1,21102,1,2037,0,106,0,1912,21202,-3,-1,-3,22201,-5,-3,-5,109,-6,2105,1,0
"""

TEST_CASES = [
    TestCase("""""", None),
]


def solve(program):
    intcode = Intcode(program)
    springscript = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""
    input = [ord(c) for c in springscript]
    try:
        while True:
            output = intcode.run(input)
            if output == 'END':
                return None
            print(chr(int(output)), end='')
    except ValueError:
        return output


if __name__ == '__main__':
    # for case in TEST_CASES:
    #     result = solve(case.case)
    #     case.check(result)

    print(solve(INPUT))
