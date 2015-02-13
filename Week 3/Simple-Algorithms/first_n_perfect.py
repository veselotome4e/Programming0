n = input("Enter n: ")
n = int(n)

perfect_numbers = []
start_digit = 6

while len(perfect_numbers) != n:
    
    start = 1
    total_sum = 0

    while start < start_digit:
        if start_digit % start == 0:
            total_sum += start
        start+=1

    if total_sum == start_digit:
        perfect_numbers +=[start_digit]

    start_digit +=1

print("The first {} perfect numbers are: ".format(n))
for each in perfect_numbers:
    print(each)
     

 
