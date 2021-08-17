from mix_instruction_sets import *
from mix_misc_operators import *
from mix_loading_operators import *
from mix_storing_operators import *
from mix_arithmetic_operators import *
from mix_transfer_operators import *
from mix_comparison_operators import *
from mix_jump_operators import *

class KnuthInstructionSet(InstructionSet):
    def __init__(self):
        self.instruction_list = []
        self.instruction_list.append({"C": "0", "F": "ANY",  "name":"NOP", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "1", "F": "RANGE5",  "name":"ADD", "normF":5, "op" : ADD})
        self.instruction_list.append({"C": "1", "F": "RANGE6",  "name":"FADD", "normF":6, "op" : lambda x : 0})
        self.instruction_list.append({"C": "2", "F": "RANGE5",  "name":"SUB", "normF":5, "op" : SUB})
        self.instruction_list.append({"C": "2", "F": "RANGE6",  "name":"FSUB", "normF":6, "op" : lambda x : 0})
        self.instruction_list.append({"C": "3", "F": "RANGE5",  "name":"MUL", "normF":5, "op" : MUL})
        self.instruction_list.append({"C": "3", "F": "RANGE6",  "name":"FMUL", "normF":6, "op" : lambda x : 0})
        self.instruction_list.append({"C": "4", "F": "RANGE5",  "name":"DIV", "normF":5, "op" : DIV})
        self.instruction_list.append({"C": "4", "F": "RANGE6",  "name":"FDIV", "normF":6, "op" : lambda x : 0})
        self.instruction_list.append({"C": "5", "F": "VAL0",  "name":"NUM", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "5", "F": "VAL1",  "name":"CHAR", "normF":1, "op" : lambda x : 0})
        self.instruction_list.append({"C": "5", "F": "VAL2",  "name":"HLT", "normF":2, "op" : HLT})
        self.instruction_list.append({"C": "6", "F": "VAL0",  "name":"SLA", "normF":0, "op" : SLA})
        self.instruction_list.append({"C": "6", "F": "VAL1",  "name":"SRA", "normF":1, "op" : SRA})
        self.instruction_list.append({"C": "6", "F": "VAL2",  "name":"SLAX", "normF":2, "op" : SLAX})
        self.instruction_list.append({"C": "6", "F": "VAL3",  "name":"SRAX", "normF":3, "op" : SRAX})
        self.instruction_list.append({"C": "6", "F": "VAL4",  "name":"SLC", "normF":4, "op" : SLC})
        self.instruction_list.append({"C": "6", "F": "VAL5",  "name":"SRC", "normF":5, "op" : SRC})
        self.instruction_list.append({"C": "7", "F": "ANY",  "name":"MOVE", "normF":1, "op" : MOVE})
        self.instruction_list.append({"C": "8", "F": "RANGE5",  "name":"LDA", "normF":5, "op" : LDA})
        self.instruction_list.append({"C": "9", "F": "RANGE5",  "name":"LD1", "normF":5, "op" : LD1})
        self.instruction_list.append({"C": "10", "F": "RANGE5",  "name":"LD2", "normF":5, "op" : LD2})
        self.instruction_list.append({"C": "11", "F": "RANGE5",  "name":"LD3", "normF":5, "op" : LD3})
        self.instruction_list.append({"C": "12", "F": "RANGE5",  "name":"LD4", "normF":5, "op" : LD4})
        self.instruction_list.append({"C": "13", "F": "RANGE5",  "name":"LD5", "normF":5, "op" : LD5})
        self.instruction_list.append({"C": "14", "F": "RANGE5",  "name":"LD6", "normF":5, "op" : LD6})
        self.instruction_list.append({"C": "15", "F": "RANGE5",  "name":"LDX", "normF":5, "op" : LDX})
        self.instruction_list.append({"C": "16", "F": "RANGE5",  "name":"LDAN", "normF":5, "op" : LDAN})
        self.instruction_list.append({"C": "17", "F": "RANGE5",  "name":"LD1N", "normF":5, "op" : LD1N})
        self.instruction_list.append({"C": "18", "F": "RANGE5",  "name":"LD2N", "normF":5, "op" : LD2N})
        self.instruction_list.append({"C": "19", "F": "RANGE5",  "name":"LD3N", "normF":5, "op" : LD3N})
        self.instruction_list.append({"C": "20", "F": "RANGE5",  "name":"LD4N", "normF":5, "op" : LD4N})
        self.instruction_list.append({"C": "21", "F": "RANGE5",  "name":"LD5N", "normF":5, "op" : LD5N})
        self.instruction_list.append({"C": "22", "F": "RANGE5",  "name":"LD6N", "normF":5, "op" : LD6N})
        self.instruction_list.append({"C": "23", "F": "RANGE5",  "name":"LDXN", "normF":5, "op" : LDXN})
        self.instruction_list.append({"C": "24", "F": "RANGE5",  "name":"STA", "normF":5, "op" : STA})
        self.instruction_list.append({"C": "25", "F": "RANGE5",  "name":"ST1", "normF":5, "op" : ST1})
        self.instruction_list.append({"C": "26", "F": "RANGE5",  "name":"ST2", "normF":5, "op" : ST2})
        self.instruction_list.append({"C": "27", "F": "RANGE5",  "name":"ST3", "normF":5, "op" : ST3})
        self.instruction_list.append({"C": "28", "F": "RANGE5",  "name":"ST4", "normF":5, "op" : ST4})
        self.instruction_list.append({"C": "29", "F": "RANGE5",  "name":"ST5", "normF":5, "op" : ST5})
        self.instruction_list.append({"C": "30", "F": "RANGE5",  "name":"ST6", "normF":5, "op" : ST6})
        self.instruction_list.append({"C": "31", "F": "RANGE5",  "name":"STX", "normF":5, "op" : STX})
        self.instruction_list.append({"C": "32", "F": "RANGE5",  "name":"STJ", "normF":2, "op" : STJ})
        self.instruction_list.append({"C": "33", "F": "RANGE5",  "name":"STZ", "normF":5, "op" : STZ})
        self.instruction_list.append({"C": "34", "F": "ANY",  "name":"JBUS", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "35", "F": "ANY",  "name":"IOC", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "36", "F": "ANY",  "name":"IN", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "37", "F": "ANY",  "name":"OUT", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "38", "F": "ANY",  "name":"JRED", "normF":0, "op" : lambda x : 0})
        self.instruction_list.append({"C": "39", "F": "VAL0",  "name":"JMP", "normF":0, "op" : JMP})
        self.instruction_list.append({"C": "39", "F": "VAL1",  "name":"JSJ", "normF":1, "op" : JSJ})
        self.instruction_list.append({"C": "39", "F": "VAL2",  "name":"JOV", "normF":2, "op" : JOV})
        self.instruction_list.append({"C": "39", "F": "VAL3",  "name":"JNOV", "normF":3, "op" : JNOV})
        self.instruction_list.append({"C": "39", "F": "VAL4",  "name":"JL", "normF":4, "op" : JL})
        self.instruction_list.append({"C": "39", "F": "VAL5",  "name":"JE", "normF":5, "op" : JE})
        self.instruction_list.append({"C": "39", "F": "VAL6",  "name":"JG", "normF":6, "op" : JG})
        self.instruction_list.append({"C": "39", "F": "VAL7",  "name":"JGE", "normF":7, "op" : JGE})
        self.instruction_list.append({"C": "39", "F": "VAL8",  "name":"JNE", "normF":8, "op" : JNE})
        self.instruction_list.append({"C": "39", "F": "VAL9",  "name":"JLE", "normF":9, "op" : JLE})
        self.instruction_list.append({"C": "40", "F": "VAL0",  "name":"JAN", "normF":0, "op" : JAN})
        self.instruction_list.append({"C": "40", "F": "VAL1",  "name":"JAZ", "normF":1, "op" : JAZ})
        self.instruction_list.append({"C": "40", "F": "VAL2",  "name":"JAP", "normF":2, "op" : JAP})
        self.instruction_list.append({"C": "40", "F": "VAL3",  "name":"JANN", "normF":3, "op" : JANN})
        self.instruction_list.append({"C": "40", "F": "VAL4",  "name":"JANZ", "normF":4, "op" : JANZ})
        self.instruction_list.append({"C": "40", "F": "VAL5",  "name":"JANP", "normF":5, "op" : JANP})
        self.instruction_list.append({"C": "41", "F": "VAL0",  "name":"J1N", "normF":0, "op" : J1N})
        self.instruction_list.append({"C": "41", "F": "VAL1",  "name":"J1Z", "normF":1, "op" : J1Z})
        self.instruction_list.append({"C": "41", "F": "VAL2",  "name":"J1P", "normF":2, "op" : J1P})
        self.instruction_list.append({"C": "41", "F": "VAL3",  "name":"J1NN", "normF":3, "op" : J1NN})
        self.instruction_list.append({"C": "41", "F": "VAL4",  "name":"J1NZ", "normF":4, "op" : J1NZ})
        self.instruction_list.append({"C": "41", "F": "VAL5",  "name":"J1NP", "normF":5, "op" : J1NP})
        self.instruction_list.append({"C": "42", "F": "VAL0",  "name":"J2N", "normF":0, "op" : J2N})
        self.instruction_list.append({"C": "42", "F": "VAL1",  "name":"J2Z", "normF":1, "op" : J2Z})
        self.instruction_list.append({"C": "42", "F": "VAL2",  "name":"J2P", "normF":2, "op" : J2P})
        self.instruction_list.append({"C": "42", "F": "VAL3",  "name":"J2NN", "normF":3, "op" : J2NN})
        self.instruction_list.append({"C": "42", "F": "VAL4",  "name":"J2NZ", "normF":4, "op" : J2NZ})
        self.instruction_list.append({"C": "42", "F": "VAL5",  "name":"J2NP", "normF":5, "op" : J2NP})
        self.instruction_list.append({"C": "43", "F": "VAL0",  "name":"J3N", "normF":0, "op" : J3N})
        self.instruction_list.append({"C": "43", "F": "VAL1",  "name":"J3Z", "normF":1, "op" : J3Z})
        self.instruction_list.append({"C": "43", "F": "VAL2",  "name":"J3P", "normF":2, "op" : J3P})
        self.instruction_list.append({"C": "43", "F": "VAL3",  "name":"J3NN", "normF":3, "op" : J3NN})
        self.instruction_list.append({"C": "43", "F": "VAL4",  "name":"J3NZ", "normF":4, "op" : J3NZ})
        self.instruction_list.append({"C": "43", "F": "VAL5",  "name":"J3NP", "normF":5, "op" : J3NP})
        self.instruction_list.append({"C": "44", "F": "VAL0",  "name":"J4N", "normF":0, "op" : J4N})
        self.instruction_list.append({"C": "44", "F": "VAL1",  "name":"J4Z", "normF":1, "op" : J4Z})
        self.instruction_list.append({"C": "44", "F": "VAL2",  "name":"J4P", "normF":2, "op" : J4P})
        self.instruction_list.append({"C": "44", "F": "VAL3",  "name":"J4NN", "normF":3, "op" : J4NN})
        self.instruction_list.append({"C": "44", "F": "VAL4",  "name":"J4NZ", "normF":4, "op" : J4NZ})
        self.instruction_list.append({"C": "44", "F": "VAL5",  "name":"J4NP", "normF":5, "op" : J4NP})
        self.instruction_list.append({"C": "45", "F": "VAL0",  "name":"J5N", "normF":0, "op" : J5N})
        self.instruction_list.append({"C": "45", "F": "VAL1",  "name":"J5Z", "normF":1, "op" : J5Z})
        self.instruction_list.append({"C": "45", "F": "VAL2",  "name":"J5P", "normF":2, "op" : J5P})
        self.instruction_list.append({"C": "45", "F": "VAL3",  "name":"J5NN", "normF":3, "op" : J5NN})
        self.instruction_list.append({"C": "45", "F": "VAL4",  "name":"J5NZ", "normF":4, "op" : J5NZ})
        self.instruction_list.append({"C": "45", "F": "VAL5",  "name":"J5NP", "normF":5, "op" : J5NP})
        self.instruction_list.append({"C": "46", "F": "VAL0",  "name":"J6N", "normF":0, "op" : J6N})
        self.instruction_list.append({"C": "46", "F": "VAL1",  "name":"J6Z", "normF":1, "op" : J6Z})
        self.instruction_list.append({"C": "46", "F": "VAL2",  "name":"J6P", "normF":2, "op" : J6P})
        self.instruction_list.append({"C": "46", "F": "VAL3",  "name":"J6NN", "normF":3, "op" : J6NN})
        self.instruction_list.append({"C": "46", "F": "VAL4",  "name":"J6NZ", "normF":4, "op" : J6NZ})
        self.instruction_list.append({"C": "46", "F": "VAL5",  "name":"J6NP", "normF":5, "op" : J6NP})
        self.instruction_list.append({"C": "47", "F": "VAL0",  "name":"JXN", "normF":0, "op" : JXN})
        self.instruction_list.append({"C": "47", "F": "VAL1",  "name":"JXZ", "normF":1, "op" : JXZ})
        self.instruction_list.append({"C": "47", "F": "VAL2",  "name":"JXP", "normF":2, "op" : JXP})
        self.instruction_list.append({"C": "47", "F": "VAL3",  "name":"JXNN", "normF":3, "op" : JXNN})
        self.instruction_list.append({"C": "47", "F": "VAL4",  "name":"JXNZ", "normF":4, "op" : JXNZ})
        self.instruction_list.append({"C": "47", "F": "VAL5",  "name":"JXNP", "normF":5, "op" : JXNP})
        self.instruction_list.append({"C": "48", "F": "VAL0",  "name":"INCA", "normF":0, "op" : INCA})
        self.instruction_list.append({"C": "48", "F": "VAL1",  "name":"DECA", "normF":1, "op" : DECA})
        self.instruction_list.append({"C": "48", "F": "VAL2",  "name":"ENTA", "normF":2, "op" : ENTA})
        self.instruction_list.append({"C": "48", "F": "VAL3",  "name":"ENNA", "normF":3, "op" : ENNA})
        self.instruction_list.append({"C": "49", "F": "VAL0",  "name":"INC1", "normF":0, "op" : INC1})
        self.instruction_list.append({"C": "49", "F": "VAL1",  "name":"DEC1", "normF":1, "op" : DEC1})
        self.instruction_list.append({"C": "49", "F": "VAL2",  "name":"ENT1", "normF":2, "op" : ENT1})
        self.instruction_list.append({"C": "49", "F": "VAL3",  "name":"ENN1", "normF":3, "op" : ENN1})
        self.instruction_list.append({"C": "50", "F": "VAL0",  "name":"INC2", "normF":0, "op" : INC2})
        self.instruction_list.append({"C": "50", "F": "VAL1",  "name":"DEC2", "normF":1, "op" : DEC2})
        self.instruction_list.append({"C": "50", "F": "VAL2",  "name":"ENT2", "normF":2, "op" : ENT2})
        self.instruction_list.append({"C": "50", "F": "VAL3",  "name":"ENN2", "normF":3, "op" : ENN2})
        self.instruction_list.append({"C": "51", "F": "VAL0",  "name":"INC3", "normF":0, "op" : INC3})
        self.instruction_list.append({"C": "51", "F": "VAL1",  "name":"DEC3", "normF":1, "op" : DEC3})
        self.instruction_list.append({"C": "51", "F": "VAL2",  "name":"ENT3", "normF":2, "op" : ENT3})
        self.instruction_list.append({"C": "51", "F": "VAL3",  "name":"ENN3", "normF":3, "op" : ENN3})
        self.instruction_list.append({"C": "52", "F": "VAL0",  "name":"INC4", "normF":0, "op" : INC4})
        self.instruction_list.append({"C": "52", "F": "VAL1",  "name":"DEC4", "normF":1, "op" : DEC4})
        self.instruction_list.append({"C": "52", "F": "VAL2",  "name":"ENT4", "normF":2, "op" : ENT4})
        self.instruction_list.append({"C": "52", "F": "VAL3",  "name":"ENN4", "normF":3, "op" : ENN4})
        self.instruction_list.append({"C": "53", "F": "VAL0",  "name":"INC5", "normF":0, "op" : INC5})
        self.instruction_list.append({"C": "53", "F": "VAL1",  "name":"DEC5", "normF":1, "op" : DEC5})
        self.instruction_list.append({"C": "53", "F": "VAL2",  "name":"ENT5", "normF":2, "op" : ENT5})
        self.instruction_list.append({"C": "53", "F": "VAL3",  "name":"ENN5", "normF":3, "op" : ENN5})
        self.instruction_list.append({"C": "54", "F": "VAL0",  "name":"INC6", "normF":0, "op" : INC6})
        self.instruction_list.append({"C": "54", "F": "VAL1",  "name":"DEC6", "normF":1, "op" : DEC6})
        self.instruction_list.append({"C": "54", "F": "VAL2",  "name":"ENT6", "normF":2, "op" : ENT6})
        self.instruction_list.append({"C": "54", "F": "VAL3",  "name":"ENN6", "normF":3, "op" : ENN6})
        self.instruction_list.append({"C": "55", "F": "VAL0",  "name":"INCX", "normF":0, "op" : INCX})
        self.instruction_list.append({"C": "55", "F": "VAL1",  "name":"DECX", "normF":1, "op" : DECX})
        self.instruction_list.append({"C": "55", "F": "VAL2",  "name":"ENTX", "normF":2, "op" : ENTX})
        self.instruction_list.append({"C": "55", "F": "VAL3",  "name":"ENNX", "normF":3, "op" : ENNX})
        self.instruction_list.append({"C": "56", "F": "RANGE5",  "name":"CMPA", "normF":5, "op" : CMPA})
        self.instruction_list.append({"C": "56", "F": "VAL6",  "name":"FCMP", "normF":6, "op" : lambda x : 0})
        self.instruction_list.append({"C": "57", "F": "RANGE5",  "name":"CMP1", "normF":5, "op" : CMP1})
        self.instruction_list.append({"C": "58", "F": "RANGE5",  "name":"CMP2", "normF":5, "op" : CMP2})
        self.instruction_list.append({"C": "59", "F": "RANGE5",  "name":"CMP3", "normF":5, "op" : CMP3})
        self.instruction_list.append({"C": "60", "F": "RANGE5",  "name":"CMP4", "normF":5, "op" : CMP4})
        self.instruction_list.append({"C": "61", "F": "RANGE5",  "name":"CMP5", "normF":5, "op" : CMP5})
        self.instruction_list.append({"C": "62", "F": "RANGE5",  "name":"CMP6", "normF":5, "op" : CMP6})
        self.instruction_list.append({"C": "63", "F": "RANGE5",  "name":"CMPX", "normF":5, "op" : CMPX})
        self.invalid_opcode = {"C" : "5", "normF": "VAL2", "F": 2}
        
        self.known_instructions = {}        
        self.build_instructions(self.instruction_list)
        self.invalid_instruction = "INVALID INSTRUCTION"        
        self.invalid_operation = HLT
                