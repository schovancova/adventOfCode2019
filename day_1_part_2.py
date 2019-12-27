import os
import sys

def get_total_fuel(mass):
    total_fuel = 0
    while mass >= 0:
        mass = int(int(mass)/3) - 2
        total_fuel += mass if mass > 0 else 0 
    return total_fuel

   

f = open(os.path.join(sys.path[0], "testinput"), "r")
line = f.readline()
result = 0
while line:
    result += get_total_fuel(int(line))
    line = f.readline()
print(result)

