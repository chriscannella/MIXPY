from xitwords import XitWord

def NUM(mix_machine):
    data = []
    data += mix_machine.X.word
    data += mix_machine.A.word
    data = [str(entry % 10) for entry in data][::-1]
    num_str = ''.join(data)
    if mix_machine.A.toggle:
        num_str = '-' + num_str
    mix_machine.A.read(int(num_str))
    return 10

def CHAR(mix_machine):
    outWord = XitWord(word_length=10, base=mix_machine.base)
    outWord[6:11] = mix_machine.A[1:6]
    num_str = (10 - len(str(int(outWord))))*'0' + str(int(outWord))
    print(num_str)
    data = [int('3' + char) for char in num_str][::-1]
    print(data)
    outWord.read(data)
    mix_machine.A[1:6] = outWord[1:6]
    mix_machine.X[1:6] = outWord[6:11]
    return 10



