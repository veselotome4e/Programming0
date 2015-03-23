def is_string_palindrom(string):
    string = string.lower()
    delimiters = [',','.','!','?',':','-',"'",'"', ' ']

    modified = [x for x in string if x not in delimiters]
    modified = from_list_to_string(modified)

    return modified == modified[::-1]


def from_list_to_string(l):
    s = ""
    for each in l:
        s += each
    return s


print(is_string_palindrom("Az obi4am ma4 i boza"))
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaaa"))
print(is_string_palindrom(" kapak! "))
