def taken_name(surname_husband, surname_wife):

    return surname_husband in surname_wife

print(taken_name("Petrov","Petrova"))
print(taken_name("Ivanova","Tstetanova"))
print(taken_name("Petrov","Ivanova-Petrova"))
