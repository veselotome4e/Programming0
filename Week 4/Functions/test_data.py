from random import randint, shuffle


def generate_test(count):

    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]

    result = []

    for name in names:
        result += [name] * randint(1, count)

    shuffle(result)

    return result



def get_people_count(activity):
    return len(set(activity))

all_entries = generate_test(3)
print(all_entries)
print(get_people_count(all_entries))

             
