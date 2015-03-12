def forecast(days):

    events = {
        "snow": 0,
        "rain": 0,
        "sunshine": 0,
    }

    for each in days:
        events[each] += 1

    #get the values
    values = []
    for each in events:
        values.append(events[each])
 
    values = sorted(values)
    if(values[0] == values[1] and values[1] == values[2]):
        return days[len(days)-1]

    if(values[0] < values[1] and values[1] == values[2]):
        return get_key_based_on_value(events, values[0])

    biggest = values[2]
    return get_key_based_on_value(events, biggest)


def get_key_based_on_value(dictionary, key):
    for each in dictionary:
        if  dictionary[each] ==  key:
            return each

print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))