from xit_words import XitWord
def HLT(mix_machine):
    mix_machine.running = False
    return 10

def SLA(mix_machine):
    M = mix_machine.instruction.M()
    if M < 6 and M > -6:
        out_word = mix_machine.A << M
        mix_machine.A.read(out_word)
    else:
        mix_machine.A[1:6] = 0
    return 2

def SRA(mix_machine):
    M = mix_machine.instruction.M()
    if M < 6 and M > -6:
        out_word = mix_machine.A >> M
        mix_machine.A.read(out_word[0:6])
    else:
        mix_machine.A[1:6] = 0
    return 2

def SLAX(mix_machine):
    M = mix_machine.instruction.M()
    if M < 11 and M > -11:
        outWord = XitWord(word_length=10, base=mix_machine.base)
        outWord[0:6] = mix_machine.A
        outWord[6:11] = mix_machine.X[1:6]
        outWord = outWord << M
        return_word = XitWord(word_length=10, base=mix_machine.base)
        return_word.read(outWord)
        mix_machine.A[1:6] = return_word[1:6]
        mix_machine.X[1:6] = return_word[6:11]
    else:
        mix_machine.A[1:6] = 0
        mix_machine.X[1:6] = 0
    return 2

def SRAX(mix_machine):
    M = mix_machine.instruction.M()
    if M < 11 and M > -11:
        outWord = XitWord(word_length=10, base=mix_machine.base)
        outWord[0:6] = mix_machine.A
        outWord[6:11] = mix_machine.X[1:6]
        outWord = outWord >> M
        return_word = XitWord(word_length=10, base=mix_machine.base)
        return_word.read(outWord[0:11])
        mix_machine.A[1:6] = return_word[1:6]
        mix_machine.X[1:6] = return_word[6:11]
    else:
        mix_machine.A[1:6] = 0
        mix_machine.X[1:6] = 0
    return 2

def SLC(mix_machine):
    M=mix_machine.instruction.M()
    M = M % 10
    data = []
    data += mix_machine.X.word
    data += mix_machine.A.word
    data = data[::-1]
    data = data[M:] + data[:M]
    data  = data[::-1]
    return_word = XitWord(word_length=10, base=mix_machine.base)
    return_word.read(data)
    mix_machine.A[1:6] = return_word[1:6]
    mix_machine.X[1:6] = return_word[6:11]
    return 2

def SRC(mix_machine):
    M=mix_machine.instruction.M()
    M = M % 10
    data = []
    data += mix_machine.X.word
    data += mix_machine.A.word
    data = data[M:] + data[:M]
    return_word = XitWord(word_length=10, base=mix_machine.base)
    return_word.read(data)
    mix_machine.A[1:6] = return_word[1:6]
    mix_machine.X[1:6] = return_word[6:11]
    return 2

def MOVE(mix_machine):
    num_moved = mix_machine.instruction.F()
    print(num_moved)
    starting_loc = mix_machine.instruction.M()
    transfer_loc = int(mix_machine.index_registers[0])
    for offset in range(0,num_moved):
        mix_machine.memory[transfer_loc + offset].read(mix_machine.memory[starting_loc + offset])
    mix_machine.index_registers[0] += XitWord(int(num_moved), word_length=2, base=mix_machine.base)
    return 1 + 2*num_moved


