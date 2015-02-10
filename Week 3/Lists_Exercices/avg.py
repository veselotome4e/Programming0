n = input("Enter count of numbers: ")
n = int(n)

count = 1
all_nums = []
total_sum = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    total_sum += number
    all_nums += [number]
    count += 1

print("Avg is: {}".format(total_sum/len(all_nums)))
