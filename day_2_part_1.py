import os
import sys

f = open(os.path.join(sys.path[0], "testinput"), "r")
intcode = [int(x) for x in  (f.readline()).split(",")]
position = 0
while True:
    opcode = intcode[position]
    if opcode == 99:
        break
    first_op = intcode[intcode[position+1]]
    second_op = intcode[intcode[position+2]]
    intcode[intcode[position+3]] = first_op + second_op if opcode == 1 else first_op * second_op
    position += 4
print(intcode[0])