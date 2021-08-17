def enter_address(mix_machine, register):
    M = mix_machine.instruction.M_word()
    register.read(M)
    return None

def enter_negative_address(mix_machine, register):
    M = mix_machine.instruction.M_word()
    register.read(-M)
    return None

def increment_register(mix_machine, register):
    M = mix_machine.instruction.M_word()
    register += M
    if register.overflow:
        mix_machine.overflow = True
        register.overflow = False
    return None

def decrement_register(mix_machine, register):
    M = mix_machine.instruction.M_word()
    register -= M
    if register.overflow:
        mix_machine.overflow = True
        register.overflow = False
    return None