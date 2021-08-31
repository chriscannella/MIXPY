from mixmachine import MixMachine
test_machine = MixMachine(64)
test_machine.instruction.read([True, 8, 5, 4, 2000 % 64, 2000 / 64])
print(test_machine.instruction)

test_machine.instruction.read("LDA 2000,2(0:3)")
print(test_machine.instruction.data)
print(test_machine.instruction)

test_machine.instruction.read("LDA 2000,2(1:3)")
print(test_machine.instruction.data)
print(test_machine.instruction)

test_machine.instruction.read("LDA 2000(1:3)")
print(test_machine.instruction.data)
print(test_machine.instruction)

test_machine.instruction.read("LDA 2000")
print(test_machine.instruction.data)
print(test_machine.instruction)

test_machine.instruction.read("LDA -2000,4")
print(test_machine.instruction.data)
print(test_machine.instruction)

test_machine.instruction.read("HLT 0")
print(test_machine.instruction.data)
print(test_machine.instruction)

test_machine.memory[2000].read([True, 4,5,3,16,1])
test_machine.instruction.read("LDA 2000(1:5)")
test_machine.instruction()
print(test_machine.A)


