from mix_storing_utils import store_register, store_zero

def STA(mix_machine):
    return store_register(mix_machine, mix_machine.A)

def STX(mix_machine):
    return store_register(mix_machine, mix_machine.X)

def ST1(mix_machine):
    return store_register(mix_machine, mix_machine.index_registers[0])

def ST2(mix_machine):
    return store_register(mix_machine, mix_machine.index_registers[1])

def ST3(mix_machine):
    return store_register(mix_machine, mix_machine.index_registers[2])

def ST4(mix_machine):
    return store_register(mix_machine, mix_machine.index_registers[3])

def ST5(mix_machine):
    return store_register(mix_machine, mix_machine.index_registers[4])

def ST6(mix_machine):
    return store_register(mix_machine, mix_machine.index_registers[5])

def STJ(mix_machine):
    return store_register(mix_machine, mix_machine.J)

def STZ(mix_machine):
    return store_zero(mix_machine)