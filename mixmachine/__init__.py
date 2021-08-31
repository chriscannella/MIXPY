from xitwords import XitWord
from mixmachine.io import MixIODevice
from mixmachine.instruction import MixInstruction
from mixmachine.instructionset.knuth import KnuthInstructionSet


class MixMachine():
    def __init__(self, base):
        self.base = base
        self.PC = 0
        self.memory = [XitWord(0, word_length=5, base=self.base) for i in range(0, 4000)]
        self.instruction_set = KnuthInstructionSet()
        self.instruction = MixInstruction(self)
        self.A = XitWord(0, word_length=5, base=self.base)
        self.X = XitWord(0, word_length=5, base=self.base)
        self.index_registers = [XitWord(0, word_length=2, base=self.base) for i in range(0, 6)]
        self.J = XitWord(0, word_length=2, base=self.base)
        self.io = [MixIODevice(self) for i in range(0, 20)]
        self.overflow = False
        self.L = False
        self.E = False
        self.G = False
        self.running = False
