def IN(mix_machine):
    M = mix_machine.instruction.M()
    F = mix_machine.instruction.F()
    mix_machine.io[F].read_to_host(M)
    return 1

def OUT(mix_machine):
    M = mix_machine.instruction.M()
    F = mix_machine.instruction.F()
    mix_machine.io[F].write_from_host(M)
    return 1

def IOC(mix_machine):
    M = mix_machine.instruction.M()
    F = mix_machine.instruction.F()
    mix_machine.io[F].instruct(M)
    return 1

def JRED(mix_machine):
    M = mix_machine.instruction.M()
    F = mix_machine.instruction.F()
    if not mix_machine.io[F].busy:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1

def JBUS(mix_machine):
    M = mix_machine.instruction.M()
    F = mix_machine.instruction.F()
    if mix_machine.io[F].busy:
        mix_machine.J.read(mix_machine.PC)
        mix_machine.PC = M
    return 1