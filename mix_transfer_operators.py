from mix_transfer_utils import *

def ENTA(mix_machine):
    enter_address(mix_machine, mix_machine.A)
    return 1

def ENTX(mix_machine):
    enter_address(mix_machine, mix_machine.X)
    return 1

def ENT1(mix_machine):
    enter_address(mix_machine, mix_machine.index_registers[0])
    return 1

def ENT2(mix_machine):
    enter_address(mix_machine, mix_machine.index_registers[1])
    return 1

def ENT3(mix_machine):
    enter_address(mix_machine, mix_machine.index_registers[2])
    return 1

def ENT4(mix_machine):
    enter_address(mix_machine, mix_machine.index_registers[3])
    return 1

def ENT5(mix_machine):
    enter_address(mix_machine, mix_machine.index_registers[4])
    return 1

def ENT6(mix_machine):
    enter_address(mix_machine, mix_machine.index_registers[5])
    return 1

def ENNA(mix_machine):
    enter_negative_address(mix_machine, mix_machine.A)
    return 1

def ENNX(mix_machine):
    enter_negative_address(mix_machine, mix_machine.X)
    return 1

def ENN1(mix_machine):
    enter_negative_address(mix_machine, mix_machine.index_registers[0])
    return 1

def ENN2(mix_machine):
    enter_negative_address(mix_machine, mix_machine.index_registers[1])
    return 1

def ENN3(mix_machine):
    enter_negative_address(mix_machine, mix_machine.index_registers[2])
    return 1

def ENN4(mix_machine):
    enter_negative_address(mix_machine, mix_machine.index_registers[3])
    return 1

def ENN5(mix_machine):
    enter_negative_address(mix_machine, mix_machine.index_registers[4])
    return 1

def ENN6(mix_machine):
    enter_negative_address(mix_machine, mix_machine.index_registers[5])
    return 1

def INCA(mix_machine):
    increment_register(mix_machine, mix_machine.A)
    return 1

def INCX(mix_machine):
    increment_register(mix_machine, mix_machine.X)
    return 1

def INC1(mix_machine):
    increment_register(mix_machine, mix_machine.index_registers[0])
    return 1

def INC2(mix_machine):
    increment_register(mix_machine, mix_machine.index_registers[1])
    return 1

def INC3(mix_machine):
    increment_register(mix_machine, mix_machine.index_registers[2])
    return 1

def INC4(mix_machine):
    increment_register(mix_machine, mix_machine.index_registers[3])
    return 1

def INC5(mix_machine):
    increment_register(mix_machine, mix_machine.index_registers[4])
    return 1

def INC6(mix_machine):
    increment_register(mix_machine, mix_machine.index_registers[5])
    return 1

def DECA(mix_machine):
    decrement_register(mix_machine, mix_machine.A)
    return 1

def DECX(mix_machine):
    decrement_register(mix_machine, mix_machine.X)
    return 1

def DEC1(mix_machine):
    decrement_register(mix_machine, mix_machine.index_registers[0])
    return 1

def DEC2(mix_machine):
    decrement_register(mix_machine, mix_machine.index_registers[1])
    return 1

def DEC3(mix_machine):
    decrement_register(mix_machine, mix_machine.index_registers[2])
    return 1

def DEC4(mix_machine):
    decrement_register(mix_machine, mix_machine.index_registers[3])
    return 1

def DEC5(mix_machine):
    decrement_register(mix_machine, mix_machine.index_registers[4])
    return 1

def DEC6(mix_machine):
    decrement_register(mix_machine, mix_machine.index_registers[5])
    return 1