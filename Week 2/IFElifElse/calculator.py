a = int(input("Enter a: "))
b = int(input("Enter b: "))
oper = input("Enter operation: ")

result = 0
wentToElse = False

if oper == '+':
    result = a + b
elif oper == '-':
    result = a -b
elif oper == '*':
    result = a * b
elif oper == '/':
    result = a/b 
else:
    print("We do not support that operation")
    wentToElse = True

if not wentToElse:
    print("Result is:\n%d"%result)

