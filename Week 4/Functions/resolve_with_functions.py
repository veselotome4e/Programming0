def divisors(n):
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    return divisors

#print(divisors(6))
#print(divisors(9))

def sum_ints(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

def sum_divisors(n):
    all_divisors = divisors(n)
    total_sum = sum_ints(all_divisors)
    return total_sum
    
def is_perfect(n):
    if sum_divisors(n) == n:
        return True
    else:
        return False

#print(is_perfect(6))

def first_n_perfect_numbers(n):
    counter = 0
    start = 6
    perfect_nums = []
    while counter < n :
        if is_perfect(start):
            perfect_nums.append(start)
            counter +=1
        start+=1
    return perfect_nums

#print(first_n_perfect_numbers(3))
def is_prime(n):
    start = 2
    while start < n:
        if n % 2 == 0:
            return False
        start+=1
    return True

def to_digits(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    return digits

def prime_digit_in_number(n):
    digits = to_digits(n)
    exist = False
    for each_digit in digits:
        if is_prime(each_digit):
            exist = True
            break

    if exist:
        print("Yes")
    else:
        print("No")


def simple_twins(n):
    if not is_prime(n):
        print("{} is not a prime".format(n))
    else:
        upper = n + 2
        lower = n - 2
        if is_prime(upper) and is_prime(lower):
            print("Twin primes with {}: ".format(n))
            print("{}, {}".format(lower,n))
            print("{}, {}".format(n,upper))
        else:
            print("{} is prime but the others do not fullfill the requirement".format(n))

simple_twins(5)       
        
    


