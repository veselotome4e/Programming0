n = input("Enter count of numbers: ")
n = int(n)

count = 1
max_num = -9999999999999999999999999999999999999999999999999999999999

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    if number >= max_num:
        max_num = number
    count += 1

print("Max is: {}".format(max_num))
