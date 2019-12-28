import itertools
from collections import namedtuple


from utils.test_case import TestCase

INPUT = """
3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99
"""

TEST_CASES = [
    TestCase('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5|9,8,7,6,5',
             139629729),
    TestCase(
        '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10|9,7,8,5,6',
        18216)
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
    ]}

POSITION_MODE = '0'
IMMEDIATE_MODE = '1'


def run(program):
    memory = list(map(int, program.strip().split(',')))
    pc = 0
    while memory[pc] != 99:
        opcode = str(memory[pc])
        operation = OPERATIONS[int(opcode[-2:])]
        parameter_modes = opcode[:-2][::-1].ljust(operation.operands, '0')
        operands = [
            (memory[pos] if parameter_mode == POSITION_MODE else pos)
            for parameter_mode, pos
            in zip(parameter_modes, memory[pc + 1:pc + 1 + operation.operands])
        ]
        if operation.name == 'SUM':
            res = operands[0] + operands[1]
            memory[memory[pc + 3]] = res
        elif operation.name == 'MUL':
            res = operands[0] * operands[1]
            memory[memory[pc + 3]] = res
        elif operation.name == 'INPUT':
            inp = (yield)
            # print('received', inp)
            memory[memory[pc + 1]] = inp
        elif operation.name == 'OUTPUT':
            yield operands[0]
            if memory[pc + 2] == 99:
                # print('OUTPUT', operands[0])
                return operands[0]
        elif operation.name == 'JUMP-IF-TRUE':
            if operands[0]:
                pc = operands[1]
                continue
        elif operation.name == 'JUMP-IF-FALSE':
            if not operands[0]:
                pc = operands[1]
                continue
        elif operation.name == 'LESS-THAN':
            memory[memory[pc + 3]] = 1 if operands[0] < operands[1] else 0
        elif operation.name == 'EQUALS':
            memory[memory[pc + 3]] = 1 if operands[0] == operands[1] else 0
        pc = pc + 1 + operation.operands
    return memory[0]


def solve(program, test_phase_settings=None):
    max_energy = 0
    for phase_settings in [test_phase_settings] if test_phase_settings else itertools.permutations([5, 6, 7, 8, 9]):
        amplifiers = [run(program) for _ in phase_settings]
        for amplifier, phase in zip(amplifiers, phase_settings):
            amplifier.__next__()
            amplifier.send(phase)
        energy = 0
        finished = False
        while not finished:
            for amplifier in amplifiers:
                try:
                    energy = amplifier.send(energy)
                    amplifier.__next__()
                except StopIteration as e:
                    finished = True
        if energy > max_energy:
            max_energy = energy
            max_energy_phase_settings = phase_settings
    print(max_energy_phase_settings)
    return max_energy


if __name__ == '__main__':
    for case in TEST_CASES:
        program, phase_settings = case.case.split('|')
        phase_settings = list(map(int, phase_settings.strip().split(',')))
        result = solve(program, phase_settings)
        case.check(result)

    print(solve(INPUT))
