import itertools
from collections import namedtuple

from utils.test_case import TestCase

INPUT = """
3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99
"""

TEST_CASES = [
    TestCase('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', 43210),  # 4,3,2,1,0
    TestCase('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0', 54321),  # 0,1,2,3,4
    TestCase('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0',
             65210),  # 1,0,4,3,2
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


def run(program, input_values):
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
            memory[memory[pc + 1]] = input_values.pop(0)
        elif operation.name == 'OUTPUT':
            if memory[pc + 2] == 99:
                # print('OUTPUT', operands[0])
                return operands[0]
            assert operands[0] == 0
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


def solve(program):
    max_energy = 0
    for phase_settings in itertools.permutations([0, 1, 2, 3, 4]):
        energy = 0
        for phase in phase_settings:
            energy = run(program, [phase, energy])
        if energy > max_energy:
            max_energy = energy
            max_energy_phase_settings = phase_settings
    print(max_energy_phase_settings)
    return max_energy


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
