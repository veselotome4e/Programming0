def swap(i, j, items):
    tmp = items[i]
    items[i] = items[j]
    items[j] = tmp

def find_index_smallest_element(start_index, items):

    n = len(items)
    smallest = items[start_index]
    swapped = False
    index = -1

    for i in range(start_index+1, n):
        if items[i] < smallest:
            smallest = items[i]
            index = i
            swapped = True

    if swapped == True:
        return index

    return start_index

def selection_sort(number):

    n = len(number)

    for i in range(0, n-1):
        index = find_index_smallest_element(i, number)
        swap(i,index,number)

l = [1,3,2,4]
l2 = [5,2,8,1,1]
l3 = [5,4,3,8,1]
selection_sort(l)
selection_sort(l2)
selection_sort(l3)
print(l)
print(l2)
print(l3)




