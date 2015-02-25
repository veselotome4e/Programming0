import math

def count_zero_neighbours(numbers, searchedNum = 0):
    
    counter = 0
    n = len(numbers)

    for i in range(0,n-1):
        for j in range(i+1,n):
            current_check = numbers[i] + numbers[j]
            if current_check == searchedNum:
                counter +=1
                
    return counter


#print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))

def count_zero_pairs(numbers, looked_sum = 0):

    counter = 0
    n = len(numbers)

    for i in range(0,n):
        for j in range(i,n):
            current_check = numbers[i] + numbers[j]
            if current_check == looked_sum:
                counter +=1
                
    return counter
    
#print(count_zero_pairs([0, 2, -2, 5, 10]))

def prime_pair(numbers):

    n = len(numbers)
    
    for i in range(0,n):
        for j in range(i,n):
            current_check = numbers[i] + numbers[j]
            if is_prime(current_check):
                return True

    return False
    
def is_prime(num):
    prime = True
    start = 2
    
    while start <= math.sqrt(num):
        if num % start == 0:
            prime = False
            break
        start +=1

    return prime

#print(prime_pair([1,2,3,4,5]))

 
