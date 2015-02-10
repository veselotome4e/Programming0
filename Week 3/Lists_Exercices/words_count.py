word = input("Enter word: ")
n = input("Enter n: ")
n = int(n)

count = 1
words_counter = 0
all_words = []
 
while count <= n:
    current_word = input("Enter word: ")
    if word == current_word:
        words_counter+=1     
    count += 1

print("{} is found: {}".format(word,words_counter))
