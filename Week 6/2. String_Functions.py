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
#print(join("PP", ["line1", "line2"]))
#print(join("\n", ["line1", "line2"]))

def startswith(search, string):

    n = len(search)
    begining_string = string[0:n]

    return search == begining_string


#print(startswith("Py", "Python"))
#print(startswith("py", "Python"))
#print(startswith("baba", "asdbaba"))

def endswith(search, string):

    search_reversed = reverse(searssch)
    search_string = reverse(string)

    return startswith(search_reversed, search_string)


#print(endswith(".py", "hello.py"))
#print(endswith("kapak", "babakapak"))
#print(endswith(" ", "Python   "))
#print(endswith("py", "python"))

def trim(string):

    l = []
    for each_char in string:
        l.append(each_char)

    n = len(l)
    for each_index in range(1, n-1):
        if l[each_index] == " ":
            #check the neighbours
            if l[each_index-1] == " " and l[each_index+1] == " ":
                del(l[each_index])
             
    print(l)


#print(trim("   asda   "))
#print(trim(" spacious    "))
print(trim("no here but yes at end   "))
#print(trim("                      "))
#print(trim("python"))
