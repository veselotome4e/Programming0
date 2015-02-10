n = input("Enter count of numbers: ")
n = int(n)

count = 1
min_num = 9999999999999999999999999999999999999999999999999999999999

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    if number <= min_num:
        min_num = number
    count += 1

print("Min is: {}".format(min_num))
