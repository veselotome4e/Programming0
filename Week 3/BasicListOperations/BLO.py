l = [1]
l = [1,2,3]
l = []
l = [True,True,True]
l = ["Python","Django"]
l = ["Iliya","Fedev","Belichev"]
l = ["Christian","Recoba","Samorano","Peshev","Brat mu"]
l = ["C#","C","C++","JavaScript","Python","Java","PHP"]

languages = ["Python", "Ruby"]
languages += ["C++"]
languages += ["Java"]
languages += ["C#"]


languages[0] = "Haskell"
languages[len(languages)-1] = "Go"

first = languages[0]
second = languages[1]
fifth = languages[4]
languages[0] = "F"
last = languages[len(languages)-1]

if "Haskell" in languages:
    print("Got Haskell")

if "Ruby" in languages:
    print("Got Ruby")

if "Go" in languages:
    print("Got Go")

if "Rust" in languages:
    print("Got Rust")


a = [1,2,3]
b = [4,5,6]
c = [1]
d = [8,8,10]

f = a + b + c + d
g = a + b
h = c + d
w = a + a

