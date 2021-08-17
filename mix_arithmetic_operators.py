from xit_words import XitWord

def ADD(mix_machine):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    mix_machine.A += mix_machine.memory[M][field_spec[0]:field_spec[1]]
    if mix_machine.A.overflow:
        mix_machine.overflow = True
        mix_machine.A.overflow = False
    return 2

def SUB(mix_machine):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    mix_machine.A -= mix_machine.memory[M][field_spec[0]:field_spec[1]]
    if mix_machine.A.overflow:
        mix_machine.overflow = True
        mix_machine.A.overflow = False
    return 2

def MUL(mix_machine):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    outWord = XitWord(word_length=10, base=mix_machine.base)
    outWord.read(mix_machine.A)
    outWord *= mix_machine.memory[M][field_spec[0]:field_spec[1]]
    if outWord.overflow:
        mix_machine.overflow = True
    mix_machine.A.read(outWord[0:6])
    mix_machine.X.read(outWord[6:11])
    mix_machine.A.toggle = outWord.toggle
    mix_machine.X.toggle = outWord.toggle
    return 10

def DIV(mix_machine):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    outWord = XitWord(word_length=10, base=mix_machine.base)
    outWord[0:6] = mix_machine.A
    returnToggle = mix_machine.A.toggle
    outWord[6:11] = mix_machine.X[1:6]
    outWord.toggle = mix_machine.A.toggle
    result, remainder = divmod(outWord, mix_machine.memory[M][field_spec[0]:field_spec[1]])
    mix_machine.A.read(result)
    mix_machine.X.read(remainder)
    if mix_machine.A.overflow:
        mix_machine.overflow = True
        mix_machine.A.overflow = False
    if mix_machine.memory[M][field_spec[0]:field_spec[1]] == 0:
        mix_machine.overflow = True
    mix_machine.X.toggle = returnToggle
    return 12