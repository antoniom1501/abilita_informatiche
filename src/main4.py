import sys
import numpy as np

l = []
with open('src/input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    #print(line)
    if len(line) > 0:
      l.append(list(map(int, line.split(','))))
print(l)
print()
fin = open('src/input.txt','r')
a=[]
for line in fin.readlines():
    a.append( [ int (x) for x in line.split(',') ] )
print(a)
print()

input = np.loadtxt("src/input.txt", dtype='i',delimiter=',')
print(input)
