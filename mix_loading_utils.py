def load_register(mix_machine, register):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    register.read(mix_machine.contents(M)[field_spec[0]:field_spec[1]])
    return 2

def load_register_negative(mix_machine, register):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    register.read(-mix_machine.contents(M)[field_spec[0]:field_spec[1]])
    return 2