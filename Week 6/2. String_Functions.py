def reverse(string):

    s = ""
    n = len(string)
    
    for each_index in range(0, n):
        s+= string[n-1-each_index]

    return s

#print(reverse("Python"))
#print(reverse("kapak"))
#print(reverse(""))

def join(delimiter, items):

    s = ""
    n = len(items)

    for each_index in range(0,n):
        combination = ""
        if each_index == n-1:          
            combination = str(items[each_index])
        else:
            combination = str(items[each_index]) + delimiter
        s += combination

    return s

#print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))
#print(join("\n", ["line1", "line2"]))

def startswith(search, string):

    n = len(search)
    begining_string = string[0:n]

    return search == begining_string


#print(startswith("Py", "Python"))
#print(startswith("py", "Python"))
#print(startswith("baba", "asdbaba"))

def endswith(search, string):

    search_reversed = reverse(search)
    search_string = reverse(string)

    return startswith(search_reversed, search_string)


#print(endswith(".py", "hello.py"))
#print(endswith("kapak", "babakapak"))
#print(endswith(" ", "Python   "))
#print(endswith("py", "python"))

def trim(string):

    n = len(string)
    white_space = " "
    s = ""

    for each in range(0, n):
        if string[each] == white_space and each + 1 < n and string[each+1] == white_space:
                current_index = each
                while string[current_index] == white_space:
                    current_index +=1 
                    if current_index < n:
                        break
        else:
            s += string[each]

    if  len(s) > 1 and s[0] == white_space:
        s = s[1:]

    if  len(s) > 0 and s[len(s)-1] == white_space:
        s = s[:len(s)-1]

    return "The trim new string: {}".format(s) +  " Length: " + str(len(s))


print(trim("   asda   "))
print(trim(" spacious    "))
print(trim("no here but yes at end   "))
print(trim("                      "))
print(trim("python"))
