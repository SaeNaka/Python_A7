import sys
args = sys.argv

input1 = int(args[1])
input2 = args[2]

animal = ["giraffe","tiger","zebra","elephant","lion"]
animal.insert (input1,input2)
animal.pop()
animal.sort()
print(animal)

