def jump_register_zero(mix_machine, register):
    if register == 0:
        M = mix_machine.instruction.M()
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return None


def jump_register_positive(mix_machine, register):
    if register > 0:
        M = mix_machine.instruction.M()
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return None


def jump_register_negative(mix_machine, register):
    if register < 0:
        M = mix_machine.instruction.M()
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return None


def jump_register_nonzero(mix_machine, register):
    if register != 0:
        M = mix_machine.instruction.M()
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return None


def jump_register_nonnegative(mix_machine, register):
    if register > -1:
        M = mix_machine.instruction.M()
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return None

def jump_register_nonpositive(mix_machine, register):
    if register < 1:
        M = mix_machine.instruction.M()
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return None