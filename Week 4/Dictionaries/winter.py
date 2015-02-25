def winter_is_coming(seasons):

    n = len(seasons)
   #take the first occurence of winter in season
    winter = "winter"
    index = -1

    for i in range(0, n):
        if seasons[i] == winter:
            index = i
            break

    #if the index is still -1, winter is totally missing
    if index == -1:
        return False

    #trying to find a sequence of 5 different elements out of summer
    current_seq = 0
    needed_seq = 5
    for i in range(index+1, n):
        if seasons[i] != winter:
            current_seq +=1
            if current_seq == needed_seq:
                return True
        else:
            current_seq = 0

    return False


print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "srping"]))
