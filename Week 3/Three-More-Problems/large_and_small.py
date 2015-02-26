import math

n = input("Enter n: ")
n = int(n)

#take all digits from n
def take_all_digits(n):

    digits = []
    divider = 10
    while n > 0:
        current_digit = n % divider
        digits.append(current_digit)
        n //= divider

    return digits


digits = take_all_digits(12311984324)

#Sort them increasing and decreasing
digits_acsending = sorted(digits)
digits_descending = sorted(digits, reverse=True)

#Conver the digits into biggest/smallest value based on the power of the length
def get_value_from_digits(numbers):

    power = len(numbers) - 1
    total = 0

    for each in numbers:
        result = math.pow(10,power) * each
        total += result
        power -= 1

    return int(total)


print(get_value_from_digits(digits_acsending))
print(get_value_from_digits(digits_descending))
        
