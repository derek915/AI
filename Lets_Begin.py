import numpy as np
with open("Adjectives.txt") as Adj: #in read mode, not in write mode, careful
rd = Adj.readlines()

adjs = []

for line in rd:
   adjs.append(line.split())

print(adjs)
