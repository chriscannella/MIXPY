from xit_words import XitWord

def store_register(mix_machine, register):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    outWord = XitWord(word_length=5, base=mix_machine.base)
    outWord.read(mix_machine.contents(M))
    original_toggle = outWord.toggle
    outWord[field_spec[0]:field_spec[1]] = register
    mix_machine.memory[M] = [outWord.toggle] + outWord.word
    if field_spec[0] == 0:
        mix_machine.memory[M][0] = register.toggle
    else:
        mix_machine.memory[M][0] = original_toggle
    return 2

def store_zero(mix_machine):
    M = mix_machine.instruction.M()
    field_spec = mix_machine.instruction.field_spec()
    outWord = XitWord(word_length=5, base=mix_machine.base)
    outWord.read(mix_machine.contents(M))
    original_toggle = outWord.toggle
    zero = XitWord(word_length=5, base=mix_machine.base)
    zero.read(0)
    outWord[field_spec[0]:field_spec[1]] = zero
    mix_machine.memory[M] = [outWord.toggle] + outWord.word
    if field_spec[0] == 0:
        mix_machine.memory[M][0] = zero.toggle
    else:
        mix_machine.memory[M][0] = original_toggle
    return 2