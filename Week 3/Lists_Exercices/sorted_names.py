n = input("Enter n: ")
n = int(n)

count = 1
all_words = []
 
while count <= n:
    current_word = input("Enter word: ")
    all_words += [current_word]
    count += 1


assorted = False
while not assorted:
    assorted = True
    for i in range(len(all_words)-1):
        if all_words[i] >= all_words[i+1]:
            tmp = all_words[i]
            all_words[i] = all_words[i+1]
            all_words[i+1] = tmp
            assorted = False
            
print("Sorted names are: ")
for each_word in all_words:
    print(each_word)

 

