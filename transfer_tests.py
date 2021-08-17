from mix_machine import MixMachine
test_machine = MixMachine(64)


test_machine.instruction.read("ENTA -0,1")
test_machine.instruction()
print(test_machine.A)
print(test_machine.A.overflow)

test_machine.instruction.read("INCA 1")
test_machine.instruction()
print(test_machine.A)
print(test_machine.A.overflow)
