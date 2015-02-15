a = int(input("Enter a: "))
b = int(input("Enter b: "))

while a <= b:
    if a % 2 == 0:
        print("%d - even"%a)
    else:
        print("%d - odd"%a)
    a+=1
