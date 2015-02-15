n = input("Enter n: ")
n = int(n)

rev = 0
while n > 0:
    rev = (rev * 10) + (n%10)
    n = n //10

if rev == n:
    print("The number is a palindrom")
else:
    print("The number is not a palindrom")


