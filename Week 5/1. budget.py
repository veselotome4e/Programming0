def on_budget(books, budget):

    dictionary = {
        "books_on_budget": 0,
        "loan":0, 
        }

    books = sorted(books)
    total = sum(books)
    current_sum_books = 0

    for each_book in books:
        if each_book <= budget:
            dictionary["books_on_budget"] += 1
            budget -= each_book
            current_sum_books += each_book

    total -= (current_sum_books + budget)
    if total < 0:
        total = 0
        
    dictionary["loan"] += total

    return dictionary

print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 100], 20))
