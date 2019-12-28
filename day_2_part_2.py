import os
import sys

f = open(os.path.join(sys.path[0], "testinput"), "r")
intcode = [int(x) for x in  (f.readline()).split(",")]
print("oroginal: " + str(intcode))
main_intcode = intcode.copy()
for noun in range(0, 100):
    for verb in range (0, 100):
        intcode = main_intcode.copy()
        intcode[1] = noun
        intcode[2] = verb
        position = 0
        while True:
            opcode = intcode[position]
            if opcode == 99:
                break
            first_op = intcode[intcode[position+1]]
            second_op = intcode[intcode[position+2]]
            try:
                intcode[intcode[position+3]] = first_op + second_op if opcode == 1 else first_op * second_op
            except IndexError:
                break
            position += 4
        if intcode[0] == 19690720:
            print((100 * noun + verb))
            