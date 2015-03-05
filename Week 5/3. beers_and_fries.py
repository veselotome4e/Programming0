def max_score(beers, fries):
    
    beers = sorted(beers)
    fries = sorted(fries)
    
    max_score = 0
    n = len(beers)

    for each_index in range(0,n):
        current_mark = beers[each_index] * fries[each_index]
        max_score += current_mark

    return max_score

print(max_score([10, 11], [1, 5]))
print(max_score([5], [5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
