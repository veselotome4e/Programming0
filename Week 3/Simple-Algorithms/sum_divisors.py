n = input("Enter n: ")
n = int(n)

start = 1
total_sum = 0

while start < n:
    if n % start == 0:
        total_sum += start
    start+=1

print("The sum is: {}".format(total_sum))
 
