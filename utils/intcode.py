from collections import namedtuple, defaultdict

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


class Intcode(object):

    def __init__(self, program):
        self.memory = defaultdict(int, enumerate(map(int, program.strip().split(','))))
        self.pc = 0
        self.relative_base = 0

    def run(self, input):
        while self.memory[self.pc] != 99:
            opcode = str(self.memory[self.pc])
            operation = OPERATIONS[int(opcode[-2:])]
            parameter_modes = opcode[:-2][::-1].ljust(operation.operands, '0')
            operands = []
            for parameter_mode, pos in zip(parameter_modes, range(self.pc + 1, self.pc + 1 + operation.operands)):
                if parameter_mode == POSITION_MODE:
                    operands.append(self.memory[self.memory[pos]])
                elif parameter_mode == RELATIVE_MODE:
                    operands.append(self.memory[self.memory[pos] + self.relative_base])
                else:
                    operands.append(self.memory[pos])
            # print(opcode, parameter_modes, operands)
            if operation.name == 'SUM':
                res = operands[0] + operands[1]
                self.memory[self.memory[self.pc + 3] + (self.relative_base if parameter_modes[2] == '2' else 0)] = res
            elif operation.name == 'MUL':
                res = operands[0] * operands[1]
                self.memory[self.memory[self.pc + 3] + (self.relative_base if parameter_modes[2] == '2' else 0)] = res
            elif operation.name == 'INPUT':
                self.memory[self.memory[self.pc + 1] + (self.relative_base if parameter_modes[0] == '2' else 0)] = int(input.pop(0))
            elif operation.name == 'OUTPUT':
                self.pc = self.pc + 1 + operation.operands
                return(str(operands[0]))
            elif operation.name == 'JUMP-IF-TRUE':
                if operands[0]:
                    self.pc = operands[1]
                    continue
            elif operation.name == 'JUMP-IF-FALSE':
                if not operands[0]:
                    self.pc = operands[1]
                    continue
            elif operation.name == 'LESS-THAN':
                self.memory[self.memory[self.pc + 3] + (self.relative_base if parameter_modes[2] == '2' else 0)] = 1 if operands[0] < operands[1] else 0
            elif operation.name == 'EQUALS':
                self.memory[self.memory[self.pc + 3] + (self.relative_base if parameter_modes[2] == '2' else 0)] = 1 if operands[0] == operands[1] else 0
            elif operation.name == 'RELATIVE-BASE-OFFSET':
                self.relative_base += operands[0]
            else:
                assert False, 'bad operation'
            self.pc = self.pc + 1 + operation.operands
        return 'END'
