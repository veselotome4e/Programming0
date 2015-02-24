def count_words(words):
    
    unique_words = set(words)
    dictionary = {}

    for each_word in unique_words:
        dictionary[each_word] = 0

    for each_word in unique_words:
        for word in words:
            if each_word == word:
                dictionary[each_word] += 1

    return dictionary
            
print(count_words(["words", "are", "meaningful", "words", "words", "are"]))
