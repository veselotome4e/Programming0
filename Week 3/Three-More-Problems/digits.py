n = input("Enter n: ")
n = int(n)

digits = []

while n > 0:
    current_digit = n % 10
    digits += [current_digit]
    n //= 10

digits.reverse()
print("List of digits is: {}".format(digits))
 
number = 0
for each in digits:
    number = number * 10 + each

print(number)
