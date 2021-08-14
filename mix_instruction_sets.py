from mix_instruction_utils import parse_F

class InstructionSet():
    def  __init__(self, instruction_list = []):
        self.known_instructions = {}
        self.instruction_list = instruction_list
        
        self.build_instructions(instruction_list)
        self.invalid_operation = None
        self.invalid_instruction = "INVALID INSTRUCTION"
        self.invalid_opcode = {"C" : "0", "normF": 0, "F": "ANY"}
    
    def build_instructions(self, instruction_list):
        for instruction in instruction_list:
            if instruction["C"] not in self.known_instructions:
                common_instructions = [listing for listing in instruction_list if listing["C"] == instruction["C"]]
                self.known_instructions[instruction["C"]] = ModifiedInstructionSet(common_instructions)
        return  

    def __call__(self, C,F):
        if str(C) in self.known_instructions:
            return self.known_instructions[str(C)](F)
        else:
            return self.invalid_operation
    
    def instruction(self, C, F):
        if str(C) in self.known_instructions:
            return self.known_instructions[str(C)].instruction(F)
        else:
            return self.invalid_instruction
        
    def find(self, instruction_name):
        matches = [instruction for instruction in self.instruction_list if instruction["name"] == instruction_name]
        if len(matches) > 0:
            matching_instruction = matches[0]
            return {"C":matching_instruction["C"], "normF":matching_instruction["normF"], "F":matching_instruction["F"]}, True
        return self.invalid_opcode, False
        
    
class ModifiedInstructionSet():
    def __init__(self, instruction_list = []):
        self.instruction_list = instruction_list
        self.known_instructions = {}
        
        self.build_instructions(instruction_list)
        self.invalid_operation = None
        self.invalid_instruction = "INVALID INSTRUCTION"
        self.known_operations = {}
        self.build_operations(instruction_list)
        
    def build_operations(self, instruction_list):
        for instruction in instruction_list:
            self.known_operations[instruction["F"]] = instruction["op"]
        return  
    
    def build_instructions(self, instruction_list):
        for instruction in instruction_list:
            self.known_instructions[instruction["F"]] = (instruction["name"], instruction["normF"])
        return 
        
    
    def __call__(self, F):
        f_val, f_range = parse_F(F)
        if "VAL" + str(f_val) in self.known_operations:
            return self.known_operations["VAL" + str(f_val)]
        ranges = [int(key[5:]) for key in self.known_operations if "RANGE" in key]
        ranges = [range for range in ranges if f_range[1] <= range]
        if ranges:
            return self.known_operations["RANGE" + str(min(ranges))]
        if "ANY" in self.known_operations:
            return self.known_operations["ANY"]   
        return self.invalid_operation
    
    def instruction(self, F):
        f_val, f_range = parse_F(F)
        if "VAL" + str(f_val) in self.known_instructions:
            return self.known_instructions["VAL" + str(f_val)]
        ranges = [int(key[5:]) for key in self.known_instructions if "RANGE" in key]
        ranges = [range for range in ranges if f_range[1] <= range]
        if ranges:
            return self.known_instructions["RANGE" + str(min(ranges))]
        if "ANY" in self.known_instructions:
            return self.known_instructions["ANY"]   
        return self.invalid_instruction
        
    
        