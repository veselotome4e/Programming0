#Hack Bulgaria Programming 101 Application
#Iliya Belichev Application 2.13.2015 

import string
from math import sqrt

def fill_tetrahedron(num):
    num = float(num)
    bulk = round((1/12 * sqrt(2) * num **3)/1000,2)
    return bulk

#Testing, expected result: 117.85
#print(fill_tetrahedron(100))

def tetrahedron_filled(tetrahedrons, water):
    tetrahedrons = sorted(tetrahedrons)
    best_Bulk = 0
    current_Bulk = 0
    counter = 0
    for each_length in tetrahedrons:
        current_Bulk += fill_tetrahedron(each_length)
        if current_Bulk <= water and current_Bulk >= best_Bulk:
            best_Bulk = current_Bulk
            counter +=1
        elif current_Bulk > water:
            break
        else:
            current_Bulk = 0
    return counter

#Testing, expected result: 2
#print(tetrahedron_filled([100, 20, 30], 10))


def get_index(char,string):
    for i in range(len(string)):
        if char == string[i]:
            return i
    
def caesar_encrypt(s, n):
    isItUpper = False
    if s.isupper():
        isItUpper = True

    s = s.lower()
    alphabet = list(string.ascii_lowercase)
    remaining = alphabet[n:]
    for i in range(n):
        remaining.append(alphabet[i])
        
    encrypt = ""
    for each in s:
        if each in alphabet:
            index = get_index(each,alphabet)
            encrypt += remaining[index]

    if isItUpper:
        return encrypt.upper()
    else:
        return encrypt

#Testing    
print(caesar_encrypt("abc", 1)) # "bcd"           
print(caesar_encrypt("ABC", 1)) # "BCD"
print(caesar_encrypt("abc", 2)) # "cde"
print(caesar_encrypt("aaa", 7)) # "hhh"
print(caesar_encrypt("xyz", 1)) # "yza"

        
                   

        
        
