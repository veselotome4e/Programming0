n = input("Enter n: ")
n = int(n)

start = 1
total_sum = 0

while start < n:
    if n % start == 0:
        total_sum += start
    start+=1

if total_sum == n:
    print("The num is perfect.")
else:
    print("The num is not perfect.")
 
