def count_vowels_consonants(word):
    
    dictionary = {
        "vowels":0,
        "consonants":0,
        }

    vowels =  "aeiouyAEIOUY"
    consonants =  "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    for each in word:
        if each in vowels:
            dictionary["vowels"] +=1
        elif each in consonants:
            dictionary["consonants"] +=1

    return dictionary

print(count_vowels_consonants("aaaAcccD"))
 
    
