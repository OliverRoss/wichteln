from itertools import permutations
from random import randint
import math


inputNames = ["Alice", "Bob", "Eve"]
if max([len(name) for name in inputNames]) > 80:
    print("Very long name detected, will be truncated to 80 chars.")

numPermutes = math.factorial(len(inputNames))
names = list(permutations(inputNames))[randint(0, numPermutes)]

mapping = {}

for index in range(len(names)):
    mapping[names[index]] = names[(index + 1) % len(names)]


for fro, to in mapping.items():
    with open(f"{fro}.txt", "w") as file:
        file.write(f"{to[:80]:<80}\n")
