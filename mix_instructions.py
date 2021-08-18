from xit_words import XitWord
from mix_instruction_utils import parse_F, parse_string_rep, valid_F
class MixInstruction():
    def __init__(self,machine):
        self.machine = machine
        self.base = machine.base
        self.data = XitWord(0, word_length=5, base=self.base)
    
    def read(self, new_data):
        if isinstance(new_data, str):
            AA = 0
            C = 0
            F = 0
            I=0
            parsed_rep = parse_string_rep(new_data)
            if parsed_rep:
                instruction_info, valid_instruction = self.machine.instruction_set.find(parsed_rep["OPNAME"])
            else:
                instruction_info = self.machine.instruction_set.invalid_opcode
                valid_instruction = False
            parsed_F = valid_F(parsed_rep, instruction_info)
            if parsed_rep and valid_instruction and parsed_F[0]:
                C = int(instruction_info["C"])
                F = parsed_F[1]
                if parsed_rep["I"]:
                    I = int(parsed_rep["I"])
                if parsed_rep["ADDRESS"]:
                    AA = int(parsed_rep["ADDRESS"])
            else:
                instruction_info = self.machine.instruction_set.invalid_opcode
                F = instruction_info["normF"]
                C = int(instruction_info["C"])
            self.data[0:3] = XitWord(AA, word_length=2, base=self.base)
            self.data[3] = XitWord(I, word_length=1, base=self.base)[1]
            self.data[4] = XitWord(F, word_length=1, base=self.base)[1]
            self.data[5] = XitWord(C, word_length=1, base=self.base)[1]
            if parsed_rep["ADDRESS"]:
                self.data[0] = ("-" in parsed_rep["ADDRESS"])
        else:
            self.data.read(new_data)
        
    def word(self):
        return XitWord(self.data, word_length=5, base=self.base)
    
    def AA(self):
        return self.data[1:3]
     
    def address(self):
        return int(self.data[0:3])
    
    def M(self):
        if self.I() > 0 and self.I()<=6:
            return int(self.data[0:3] + self.machine.index_registers[self.I() - 1])
        else:
            return int(self.data[0:3])

    def M_word(self):
        if self.I() > 0 and self.I()<=6:
            return self.data[0:3] + self.machine.index_registers[self.I() - 1]
        else:
            return self.data[0:3]

    def F(self):
        return self.data[4]
    
    def field_spec(self):
        f_val, f_spec = parse_F(self.F())
        if f_spec[0] <= f_spec[1]:
            return f_spec[0], f_spec[1] + 1
        return 0, 6
    
    def I(self):
        return self.data[3]
    
    def C(self):
        return self.data[5]              
    
    def __str__(self):
        instruction, normF = self.machine.instruction_set.instruction(self.C(), self.F())
        f_string = ""
        F = self.F()
        I = self.I()
        M = self.address()
        if F != normF:
            f_val, f_range = parse_F(F)
            f_string = "("+str(f_range[0]) +  ":" + str(f_range[1]) + ")"
        i_string = ""
        if I != 0 and I <= 6:
            i_string = "," + str(I)
        return instruction + " " + str(M) + i_string + f_string
    
    def __call__(self):
        return self.machine.instruction_set(self.C(), self.F())(self.machine)
        
        