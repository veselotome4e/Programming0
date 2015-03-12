def head(items):
    return items[0]

#print(head([1,2,3]))
#print(head(["Python"]))

def last(items):
    return items[len(items)-1]

#print(last([1, 2, 3]))
#print(last(["Python"]))

def tail(items):
    #return items[1:]
    start = 1
    end = len(items)
    l = []

    for each_index in range(1, end):
        l += [items[each_index]]

    return l

#print(tail([1, 2, 3]))
#print(tail(["Python"]))

def equal_lists(listA, listB):
    return listA == listB

#print(equal_lists([1, 2], [1, 2]))
#print(equal_lists([1, 2], [2, 1]))
#print(equal_lists([], []))

def count_items(n, items):
    #return items.count(n)
    counter = 0
    for each in items:
        if each == n:
            counter +=1
    return counter

#print(count_items(5, [1, 2, 3, 4, 5]))
#print(count_items("winter", ["winter", "winter"]))
#print(count_items(False, [True, True]))

def take(n, items):
    return items[0:n]

#print(take(2, [1, 2, 3, 4, 5]))
#print(take(3, [3, 4, 5, 6, 7, 8]))
#print(take(10, [1]))
def drop(n, items):
    return items[n:]

#print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
#print(drop(10, [1]))
def reverse(items):
    l = []
    n = len(items)
    
    for each_index in range(0, n):
        l.append(items[n-1-each_index])

    return l

#print(reverse(["Speak", "in", "reverse", "you", "must!"]))
#print(reverse([1, 2, 3]))
#print(reverse([]))
 
