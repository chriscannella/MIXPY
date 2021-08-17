from mix_comparison_utils import *
from xit_words import XitWord

def CMPA(mix_machine):
    compare_register(mix_machine, mix_machine.A)
    return 2

def CMPX(mix_machine):
    compare_register(mix_machine, mix_machine.A)
    return 2

def CMP1(mix_machine):
    compared_word = XitWord(base=mix_machine.base, word_length=5)
    compared_word.read(mix_machine.index_registers[0])
    compare_register(mix_machine, compared_word)
    return 2

def CMP2(mix_machine):
    compared_word = XitWord(base=mix_machine.base, word_length=5)
    compared_word.read(mix_machine.index_registers[1])
    compare_register(mix_machine, compared_word)
    return 2

def CMP3(mix_machine):
    compared_word = XitWord(base=mix_machine.base, word_length=5)
    compared_word.read(mix_machine.index_registers[2])
    compare_register(mix_machine, compared_word)
    return 2

def CMP4(mix_machine):
    compared_word = XitWord(base=mix_machine.base, word_length=5)
    compared_word.read(mix_machine.index_registers[3])
    compare_register(mix_machine, compared_word)
    return 2

def CMP5(mix_machine):
    compared_word = XitWord(base=mix_machine.base, word_length=5)
    compared_word.read(mix_machine.index_registers[4])
    compare_register(mix_machine, compared_word)
    return 2

def CMP6(mix_machine):
    compared_word = XitWord(base=mix_machine.base, word_length=5)
    compared_word.read(mix_machine.index_registers[5])
    compare_register(mix_machine, compared_word)
    return 2