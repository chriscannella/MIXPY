from mixmachine import MixMachine
test_machine = MixMachine(64)
test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.A.read([False,0,9,8,7,6])

test_machine.instruction.read("STA 2000")
test_machine.instruction()
print(test_machine.memory[2000])

test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.instruction.read("STA 2000(1:5)")
test_machine.instruction()
print(test_machine.memory[2000])

test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.instruction.read("STA 2000(5:5)")
test_machine.instruction()
print(test_machine.memory[2000])

test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.instruction.read("STA 2000(2:2)")
test_machine.instruction()
print(test_machine.memory[2000])

test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.instruction.read("STA 2000(2:3)")
test_machine.instruction()
print(test_machine.memory[2000])

test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.instruction.read("STA 2000(0:1)")
test_machine.instruction()
print(test_machine.memory[2000])

test_machine.memory[2000].read([True, 5,4,3,2,1])
test_machine.instruction.read("STZ 2000(2:4)")
test_machine.instruction()
print(test_machine.memory[2000])