from mix_machine import MixMachine
test_machine = MixMachine(64)

test_machine.memory[1000] = [False, 50 % 64 , 50 /64 ,5, 100 % 64, 100 /64]
test_machine.A.read([False, 150%64, 150/64,1,1234%64,1234/64])

test_machine.instruction.read("ADD 1000")
test_machine.instruction()
print(test_machine.A)
print(test_machine.A.overflow)

test_machine.memory[1000] = [True, 0 , 150 % 64 ,150 /64, 2000 % 64, 2000 /64]

test_machine.A.read([True, 9, 0,0,1234%64,1234/64])
test_machine.instruction.read("SUB 1000")
test_machine.instruction()
print(test_machine.A)
print(test_machine.A.overflow)

test_machine.memory[1000] = [False, 1,1,1,1,1]
test_machine.A.read([False, 1,1,1,1,1])
test_machine.instruction.read("MUL 1000")
test_machine.instruction()
print(test_machine.A)
print(test_machine.X)
print(test_machine.overflow)

test_machine.memory[1000] = [False, 1,1,1,1,2]
test_machine.A.read([True, 112 % 64,112 / 64,0,0,0])
test_machine.instruction.read("MUL 1000(1:1)")
test_machine.instruction()
print(test_machine.A)
print(test_machine.X)
print(test_machine.overflow)

test_machine.memory[1000] = [True, 0,0,0,0, 2]
test_machine.A.read([True, 4,112%64,112/64,0,50])
test_machine.instruction.read("MUL 1000")
test_machine.instruction()
print(test_machine.A)
print(test_machine.X)
print(test_machine.overflow)

test_machine.memory[1000] = [False, 3,0,0,0,0]
test_machine.A.read([False, 0,0,0,0,0])
test_machine.X.read([False, 17,0,0,0,0])

test_machine.instruction.read("DIV 1000")
test_machine.instruction()
print(test_machine.A)
print(test_machine.X)
print(test_machine.overflow)

test_machine.memory[1000] = [True, 0,2,0,0,0]
test_machine.A.read([True, 0,0,0,0,0])
test_machine.X.read([False, 1,3,0,1235 % 64,1235 /64])


test_machine.instruction.read("DIV 1000")
test_machine.instruction()
print(test_machine.A)
print(test_machine.X)
print(test_machine.overflow)
