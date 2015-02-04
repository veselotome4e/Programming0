from random import randint

choice = input("Enter sides: ")
firstRandomInt = randint(1,int(choice))
secondRandomInt = randint(1,int(choice))

print("First roll:\n%d"%firstRandomInt)
print("Second roll:\n%d"%secondRandomInt)

print("Sum is:\n%d"%(firstRandomInt+secondRandomInt))
