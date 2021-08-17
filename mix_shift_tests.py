from mix_machine import MixMachine
test_machine = MixMachine(64)
test_machine.A.read([True,5,4,3,2,1])
test_machine.X.read([True,10,9,8,7,6])
print(str(test_machine.A), str(test_machine.X))

test_machine.instruction.read("SRAX 1")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))

test_machine.instruction.read("SLA 2")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))

test_machine.instruction.read("SRC 4")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))

test_machine.instruction.read("SRA 2")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))

test_machine.instruction.read("SLC 501")
test_machine.instruction()
print(str(test_machine.A), str(test_machine.X))