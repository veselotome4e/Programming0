def get_all_nums(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    return digits


def large_and_small(n):
    digits_of_n = get_all_nums(n)
    print(digits_of_n.sort())
    #biggest = sorted(digits_of_n,True)
    #print(smallest)
   

large_and_small(12311984324)
    

