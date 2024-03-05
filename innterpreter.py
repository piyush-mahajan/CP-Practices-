

import sys
from itertools import count

def digit(n, num):
    return num // (10 ** (10 + n))

class Interpreter:
    def __init__(self, program):
        self._reg = [0 for _ in range(10)]
        self._mem = [0] * 1000
        self._pc = 0
        self._instructions = [self.op1000, self.op1100, self.op1200, self.op1300, self.op1400, 
                              self.op1500, self.op1600, self.op1700, self.op1800, self.op1900]
        
        for n, instruction in enumerate(program):
            self._mem[n] = instruction
        
        self._icounter = 8  # executed instructions count

    def op1000(self, opl, ope):
        if not self._reg[opl]:
            self._pc += 1
        else:
            self._pc = self._reg[ope]

    def op1100(self, opl, ope):
        self._pc = None

    def op1200(self, opi, opd):
        self._reg[opi] = opd
        self._pc += 1

    def op1300(self, opl, ope):
        self._reg[opl] = (self._reg[opl] + ope) % 1000
        self._pc += 1

    def op1400(self, op1, ope):
        self._reg[op1] = (self._reg[op1] * ope) % 1000
        self._pc += 1

    def op1500(self, opl, ope):
        self._reg[opl] = self._reg[ope]
        self._pc += 1

    def op1600(self, opl, opd):
        self._reg[opl] = (self._reg[opl] + self._reg[opd]) % 1000
        self._pc += 1

    def op1700(self, opl, ope):
        self._reg[opl] = (self._reg[opl] * self._reg[ope]) % 1000
        self._pc += 1

    def op1800(self, opt, ope):
        self._reg[opt] = self._mem[self._reg[ope]]
        self._pc += 1

    def op1900(self, opt, ope):
        self._mem[self._reg[opt]] = self._reg[ope]
        self._pc += 1

    def decode_execute(self, ins):
        family, opi, ope = digit(2, ins), digit(1, ins), digit(0, ins)
        self._instructions[family](opi, ope)

    def run(self):
        while self._pc is not None:
            ins = self._mem[self._pc]
            self.decode_execute(ins)
            self._icounter -= 1
            if self._icounter == 0:
                return 0
        return self._icounter

def load_num():
    line = sys.stdin.readline().strip()
    if not line:
        return None
    return int(line)

def load_prog():
    prog = []
    while True:
        instruction = load_num()
        if instruction is None:
            break
        prog.append(instruction)
    return prog

def main():
    nprog = load_num()

    # Discard empty line
    sys.stdin.readline()

    for n in range(nprog):
        prog = load_prog()
        inter = Interpreter(prog)
        print(inter.run())

        if n+1 < nprog:
            print()

if __name__ == "__main__":
    main()
