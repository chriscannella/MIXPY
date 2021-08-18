from mix_machine import MixMachine
test_machine = MixMachine(64)

test_machine.A.read([True, 39, 32,31,0,0])
test_machine.X.read([False, 30,30,47,57,37])

test_machine.instruction.read("NUM 0")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))
print(int(test_machine.A))
test_machine.instruction.read("INCA 1")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))
print(int(test_machine.A))
test_machine.instruction.read("CHAR 0")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))