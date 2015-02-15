random_string_taken_by_the_gods = input("Enter some string: ")

counter = 0
vowels = "aeiouyAEIOUY"

for each_char in random_string_taken_by_the_gods:
    if each_char in vowels:
        counter +=1

print(counter)
