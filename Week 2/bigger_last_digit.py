n = int(input("Enter n: "))
m = int(input("Enter m: "))

lastDigitN = n % 10
lastDigitM = m % 10

if lastDigitN > lastDigitM:
    print(n)
elif lastDigitM > lastDigitN:
    print(m)
elif lastDigitN == lastDigitM:
    if n > m:
        print(n)
    else:
        print(m)
