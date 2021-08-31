def compare_register(mix_machine, register):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    reg_val = int(register[field_spec[0]:field_spec[1]])
    mem_val = int(mix_machine.memory[M][field_spec[0]:field_spec[1]])
    if reg_val < mem_val:
        mix_machine.L = True
    elif reg_val > mem_val:
        mix_machine.G = True
    else:
        mix_machine.E = True
    return None