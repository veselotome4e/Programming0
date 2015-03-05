def sublist(list1, list2):
    
    if len(list1) == 0:
        return True

    n = len(list2)
    m = len(list1)
    
    for each in range(0, n - m + 1):
        current_sublist = list2[each:each+m]
        if current_sublist == list1:
            return True
    
    return False

    
print(sublist([1, 2, 3], [0, 0, 1, 2, 3, 5, 6]))
print(sublist(["Python"],["Python", "Django"]))
print(sublist(["Python", "Django"],["Django", "Python"]))
print(sublist([1,2], [1,0,1,2,2]))

