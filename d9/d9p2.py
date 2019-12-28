from collections import namedtuple, defaultdict

from utils.test_case import TestCase

INPUT = """
1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,1,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,0,1020,1102,1,800,1023,1101,0,388,1025,1101,0,31,1012,1102,1,1,1021,1101,22,0,1014,1101,0,30,1002,1101,0,716,1027,1102,32,1,1009,1101,0,38,1017,1102,20,1,1015,1101,33,0,1016,1101,0,35,1007,1101,0,25,1005,1102,28,1,1011,1102,1,36,1008,1101,0,39,1001,1102,1,21,1006,1101,397,0,1024,1102,1,807,1022,1101,0,348,1029,1101,0,23,1003,1101,29,0,1004,1102,1,26,1013,1102,34,1,1018,1102,1,37,1010,1101,0,27,1019,1102,24,1,1000,1101,353,0,1028,1101,0,723,1026,109,14,2101,0,-9,63,1008,63,27,63,1005,63,205,1001,64,1,64,1106,0,207,4,187,1002,64,2,64,109,-17,2108,24,6,63,1005,63,223,1105,1,229,4,213,1001,64,1,64,1002,64,2,64,109,7,2101,0,2,63,1008,63,21,63,1005,63,255,4,235,1001,64,1,64,1106,0,255,1002,64,2,64,109,-7,2108,29,7,63,1005,63,273,4,261,1106,0,277,1001,64,1,64,1002,64,2,64,109,10,1208,-5,31,63,1005,63,293,1105,1,299,4,283,1001,64,1,64,1002,64,2,64,109,2,1207,-1,35,63,1005,63,315,1106,0,321,4,305,1001,64,1,64,1002,64,2,64,109,8,1205,3,333,1106,0,339,4,327,1001,64,1,64,1002,64,2,64,109,11,2106,0,0,4,345,1106,0,357,1001,64,1,64,1002,64,2,64,109,-15,21108,40,40,6,1005,1019,379,4,363,1001,64,1,64,1106,0,379,1002,64,2,64,109,16,2105,1,-5,4,385,1001,64,1,64,1105,1,397,1002,64,2,64,109,-25,2102,1,-1,63,1008,63,26,63,1005,63,421,1001,64,1,64,1106,0,423,4,403,1002,64,2,64,109,-8,1202,9,1,63,1008,63,25,63,1005,63,445,4,429,1105,1,449,1001,64,1,64,1002,64,2,64,109,5,1207,0,40,63,1005,63,467,4,455,1106,0,471,1001,64,1,64,1002,64,2,64,109,-6,2107,24,8,63,1005,63,487,1105,1,493,4,477,1001,64,1,64,1002,64,2,64,109,15,21107,41,40,1,1005,1011,509,1106,0,515,4,499,1001,64,1,64,1002,64,2,64,109,12,1205,-1,529,4,521,1105,1,533,1001,64,1,64,1002,64,2,64,109,-20,2102,1,2,63,1008,63,29,63,1005,63,555,4,539,1105,1,559,1001,64,1,64,1002,64,2,64,109,15,1201,-9,0,63,1008,63,38,63,1005,63,579,1105,1,585,4,565,1001,64,1,64,1002,64,2,64,109,-2,21102,42,1,-3,1008,1012,44,63,1005,63,609,1001,64,1,64,1106,0,611,4,591,1002,64,2,64,109,-21,2107,29,8,63,1005,63,629,4,617,1106,0,633,1001,64,1,64,1002,64,2,64,109,15,1202,0,1,63,1008,63,30,63,1005,63,657,1001,64,1,64,1106,0,659,4,639,1002,64,2,64,109,15,21102,43,1,-8,1008,1016,43,63,1005,63,681,4,665,1105,1,685,1001,64,1,64,1002,64,2,64,109,-10,21107,44,45,-4,1005,1010,707,4,691,1001,64,1,64,1106,0,707,1002,64,2,64,109,11,2106,0,2,1001,64,1,64,1106,0,725,4,713,1002,64,2,64,109,-16,21101,45,0,8,1008,1017,43,63,1005,63,749,1001,64,1,64,1105,1,751,4,731,1002,64,2,64,109,-3,1208,2,36,63,1005,63,773,4,757,1001,64,1,64,1106,0,773,1002,64,2,64,109,18,1206,-4,787,4,779,1105,1,791,1001,64,1,64,1002,64,2,64,109,-8,2105,1,7,1001,64,1,64,1106,0,809,4,797,1002,64,2,64,109,-2,21108,46,44,2,1005,1016,825,1105,1,831,4,815,1001,64,1,64,1002,64,2,64,109,7,21101,47,0,-8,1008,1013,47,63,1005,63,857,4,837,1001,64,1,64,1105,1,857,1002,64,2,64,109,-17,1201,-4,0,63,1008,63,24,63,1005,63,883,4,863,1001,64,1,64,1105,1,883,1002,64,2,64,109,10,1206,7,895,1106,0,901,4,889,1001,64,1,64,4,64,99,21102,1,27,1,21102,1,915,0,1105,1,922,21201,1,24405,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,22102,1,1,-1,21201,-2,-3,1,21101,0,957,0,1106,0,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0
"""

TEST_CASES = [
    TestCase('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99',
             '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'),
    TestCase('1102,34915192,34915192,7,4,7,99,0', '1219070632396864'),
    TestCase('104,1125899906842624,99', '1125899906842624'),
]

Operation = namedtuple('Operation', 'name opcode operands')

OPERATIONS = {
    op.opcode: op for op in [
        Operation('SUM', 1, 3),
        Operation('MUL', 2, 3),
        Operation('INPUT', 3, 1),
        Operation('OUTPUT', 4, 1),
        Operation('JUMP-IF-TRUE', 5, 2),
        Operation('JUMP-IF-FALSE', 6, 2),
        Operation('LESS-THAN', 7, 3),
        Operation('EQUALS', 8, 3),
        Operation('RELATIVE-BASE-OFFSET', 9, 1),
    ]}

POSITION_MODE = '0'
IMMEDIATE_MODE = '1'
RELATIVE_MODE = '2'


def solve(input):
    memory = defaultdict(int, enumerate(map(int, input.strip().split(','))))
    output = []
    pc = 0
    relative_base = 0
    while memory[pc] != 99:
        opcode = str(memory[pc])
        operation = OPERATIONS[int(opcode[-2:])]
        parameter_modes = opcode[:-2][::-1].ljust(operation.operands, '0')
        # print(opcode, parameter_modes)
        # operands = [
        #     (
        #         memory[pos] if parameter_mode == POSITION_MODE else
        #         memory[pos + relative_base] if parameter_mode == RELATIVE_MODE else
        #         pos
        #     )
        #     for parameter_mode, pos
        #     in zip(parameter_modes, memory[pc+1:pc+1+operation.operands])
        # ]
        operands = []
        for parameter_mode, pos in zip(parameter_modes, range(pc + 1, pc + 1 + operation.operands)):
            if parameter_mode == POSITION_MODE:
                operands.append(memory[memory[pos]])
            elif parameter_mode == RELATIVE_MODE:
                operands.append(memory[memory[pos] + relative_base])
            else:
                operands.append(memory[pos])
        # print(opcode, parameter_modes, operands)
        if operation.name == 'SUM':
            res = operands[0] + operands[1]
            memory[memory[pc + 3] + (relative_base if parameter_modes[2] == '2' else 0)] = res
        elif operation.name == 'MUL':
            res = operands[0] * operands[1]
            memory[memory[pc + 3] + (relative_base if parameter_modes[2] == '2' else 0)] = res
        elif operation.name == 'INPUT':
            memory[memory[pc + 1] + (relative_base if parameter_modes[0] == '2' else 0)] = 2
        elif operation.name == 'OUTPUT':
            output.append(str(operands[0]))
            if memory[pc + 2] == 99:
                print('END')
                break
        elif operation.name == 'JUMP-IF-TRUE':
            if operands[0]:
                pc = operands[1]
                continue
        elif operation.name == 'JUMP-IF-FALSE':
            if not operands[0]:
                pc = operands[1]
                continue
        elif operation.name == 'LESS-THAN':
            memory[memory[pc + 3] + (relative_base if parameter_modes[2] == '2' else 0)] = 1 if operands[0] < operands[1] else 0
        elif operation.name == 'EQUALS':
            memory[memory[pc + 3] + (relative_base if parameter_modes[2] == '2' else 0)] = 1 if operands[0] == operands[1] else 0
        elif operation.name == 'RELATIVE-BASE-OFFSET':
            relative_base += operands[0]
        else:
            assert False, 'bad operation'
        pc = pc + 1 + operation.operands
    return ','.join(output)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
