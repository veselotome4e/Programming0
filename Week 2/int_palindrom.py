n = int(input("Enter n: "))
m = ""
mm = str(n)

while n >  0:
    digit = int(n % 10)
    m += str(digit)
    n = int(n / 10)

if m == mm:
    print("The number is palindrom")
else:
    print("The number is not palindrom")
