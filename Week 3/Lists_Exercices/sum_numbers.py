n = input("Enter count of numbers: ")
n = int(n)

count = 1
total_sum = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    total_sum += number 
    count += 1

print("The sum is: {}".format(total_sum))
