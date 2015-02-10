n = input("Enter count of numbers: ")
n = int(n)

count = 1
counter_for_even_numbers = 0
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    if number % 2 == 0:
        numbers = numbers + [number]
        counter_for_even_numbers +=1
    count += 1

print("Count of evens: {}".format(counter_for_even_numbers))
print("Evens are: ")
for each in numbers:
    print(each)

