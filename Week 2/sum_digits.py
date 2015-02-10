number = int(input("Enter n: "))
total = 0

while number >  0:
    digit = int(number % 10)
    total += digit
    number = int(number / 10)

print(str(total))
