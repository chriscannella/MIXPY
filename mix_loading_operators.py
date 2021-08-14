from mix_loading_utils import load_register, load_register_negative

def LDA(mix_machine):
    return load_register(mix_machine, mix_machine.A)

def LDX(mix_machine):
    return load_register(mix_machine, mix_machine.X)

def LD1(mix_machine):
    return load_register(mix_machine, mix_machine.index_registers[0])

def LD2(mix_machine):
    return load_register(mix_machine, mix_machine.index_registers[1])

def LD3(mix_machine):
    return load_register(mix_machine, mix_machine.index_registers[2])

def LD4(mix_machine):
    return load_register(mix_machine, mix_machine.index_registers[3])

def LD5(mix_machine):
    return load_register(mix_machine, mix_machine.index_registers[4])

def LD6(mix_machine):
    return load_register(mix_machine, mix_machine.index_registers[5])

def LDAN(mix_machine):
    return load_register_negative(mix_machine, mix_machine.A)

def LDXN(mix_machine):
    return load_register_negative(mix_machine, mix_machine.X)

def LD1N(mix_machine):
    return load_register_negative(mix_machine, mix_machine.index_registers[0])

def LD2N(mix_machine):
    return load_register_negative(mix_machine, mix_machine.index_registers[1])

def LD3N(mix_machine):
    return load_register_negative(mix_machine, mix_machine.index_registers[2])

def LD4N(mix_machine):
    return load_register_negative(mix_machine, mix_machine.index_registers[3])

def LD5N(mix_machine):
    return load_register_negative(mix_machine, mix_machine.index_registers[4])

def LD6N(mix_machine):
    return load_register_negative(mix_machine, mix_machine.index_registers[5])
    