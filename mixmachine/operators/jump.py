from mixmachine.utils.jump import *

def JMP(mix_machine):
    M = mix_machine.instruction.M()
    mix_machine.J.read(mix_machine.PC)
    mix_machine.PC = M
    return 1

def JSJ(mix_machine):
    M = mix_machine.instruction.M()
    mix_machine.PC = M
    return 1

def JOV(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.overflow:
        mix_machine.overflow = False
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JNOV(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.overflow:
        mix_machine.overflow = False
    else:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JL(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.L:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JE(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.E:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JG(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.G:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JGE(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.G or mix_machine.E:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JNE(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.L or mix_machine.G:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JLE(mix_machine):
    M = mix_machine.instruction.M()
    if mix_machine.L or mix_machine.E:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JAN(mix_machine):
    jump_register_negative(mix_machine, mix_machine.A)
    return 1

def JAZ(mix_machine):
    jump_register_zero(mix_machine, mix_machine.A)
    return 1

def JAP(mix_machine):
    jump_register_positive(mix_machine, mix_machine.A)
    return 1

def JANN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.A)
    return 1

def JANZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.A)
    return 1

def JANP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.A)
    return 1

def JXN(mix_machine):
    jump_register_negative(mix_machine, mix_machine.X)
    return 1

def JXZ(mix_machine):
    jump_register_zero(mix_machine, mix_machine.X)
    return 1

def JXP(mix_machine):
    jump_register_positive(mix_machine, mix_machine.X)
    return 1

def JXNN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.X)
    return 1

def JXNZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.X)
    return 1

def JXNP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.X)
    return 1

def J1N(mix_machine):
    jump_register_negative(mix_machine, mix_machine.index_registers[0])
    return 1

def J1Z(mix_machine):
    jump_register_zero(mix_machine, mix_machine.index_registers[0])
    return 1

def J1P(mix_machine):
    jump_register_positive(mix_machine, mix_machine.index_registers[0])
    return 1

def J1NN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.index_registers[0])
    return 1

def J1NZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.index_registers[0])
    return 1

def J1NP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.index_registers[0])
    return 1

def J2N(mix_machine):
    jump_register_negative(mix_machine, mix_machine.index_registers[1])
    return 1

def J2Z(mix_machine):
    jump_register_zero(mix_machine, mix_machine.index_registers[1])
    return 1

def J2P(mix_machine):
    jump_register_positive(mix_machine, mix_machine.index_registers[1])
    return 1

def J2NN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.index_registers[1])
    return 1

def J2NZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.index_registers[1])
    return 1

def J2NP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.index_registers[1])
    return 1

def J3N(mix_machine):
    jump_register_negative(mix_machine, mix_machine.index_registers[2])
    return 1

def J3Z(mix_machine):
    jump_register_zero(mix_machine, mix_machine.index_registers[2])
    return 1

def J3P(mix_machine):
    jump_register_positive(mix_machine, mix_machine.index_registers[2])
    return 1

def J3NN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.index_registers[2])
    return 1

def J3NZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.index_registers[2])
    return 1

def J3NP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.index_registers[2])
    return 1

def J4N(mix_machine):
    jump_register_negative(mix_machine, mix_machine.index_registers[3])
    return 1

def J4Z(mix_machine):
    jump_register_zero(mix_machine, mix_machine.index_registers[3])
    return 1

def J4P(mix_machine):
    jump_register_positive(mix_machine, mix_machine.index_registers[3])
    return 1

def J4NN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.index_registers[3])
    return 1

def J4NZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.index_registers[3])
    return 1

def J4NP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.index_registers[3])
    return 1

def J5N(mix_machine):
    jump_register_negative(mix_machine, mix_machine.index_registers[4])
    return 1

def J5Z(mix_machine):
    jump_register_zero(mix_machine, mix_machine.index_registers[4])
    return 1

def J5P(mix_machine):
    jump_register_positive(mix_machine, mix_machine.index_registers[4])
    return 1

def J5NN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.index_registers[4])
    return 1

def J5NZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.index_registers[4])
    return 1

def J5NP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.index_registers[4])
    return 1

def J6N(mix_machine):
    jump_register_negative(mix_machine, mix_machine.index_registers[5])
    return 1

def J6Z(mix_machine):
    jump_register_zero(mix_machine, mix_machine.index_registers[5])
    return 1

def J6P(mix_machine):
    jump_register_positive(mix_machine, mix_machine.index_registers[5])
    return 1

def J6NN(mix_machine):
    jump_register_nonnegative(mix_machine, mix_machine.index_registers[5])
    return 1

def J6NZ(mix_machine):
    jump_register_nonzero(mix_machine, mix_machine.index_registers[5])
    return 1

def J6NP(mix_machine):
    jump_register_nonpositive(mix_machine, mix_machine.index_registers[5])
    return 1
