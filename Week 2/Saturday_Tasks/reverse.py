n = input("Enter n: ")
n = int(n)

rev = 0

while n > 0:  
    rev = (10*rev) + n%10
    n =  n//10

print(rev)
    
 
