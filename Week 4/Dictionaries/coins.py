def calculate_coins(ammount):

    #dictionary with default values
    dictionary = {
        1:0,
        2:0,
        5:0,
        10:0,
        20:0,
        50:0,
        100:0
        }

    #getting the keys reversed
    keys = []
    for each in dictionary:
        keys.append(each)
    keys =  sorted(dictionary)
    keys = keys[::-1]
    
    ammount = ammount * 100      

    #removing
    for each in keys:
        if each > ammount:
            continue
        else:
            counter = 0
            while ammount >= each:
                ammount = ammount - each
                dictionary[each] +=1

    return dictionary
                
    
print(calculate_coins(0.53))
print(calculate_coins(8.94))
 
