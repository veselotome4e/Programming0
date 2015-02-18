from random import randint

# Step 1. Get the boundaries
min_bound = input("Enter minimum boundary for the random numbers: ")
max_bound = input("Enter maximum boundary for the random numbers: ")

min_bound = int(min_bound)
max_bound = int(max_bound)


# Step 2. Fill the list with random numbers
def fill_list_with_randoms(min_bound,max_bound):
    numbers = []

    for i in range(10):
        random_number = randint(min_bound,max_bound)
        numbers = [random_number] + numbers

    return numbers

# Step 3. Sort the array, for our example we use Bubble Sort
def bubble_sort(numbers):
    assorted = False

    while not assorted:
        assorted = True

        for num in range(len(numbers)-1):
            if numbers[num] > numbers[num+1]:
                tmp = numbers[num]
                numbers[num] = numbers[num+1]
                numbers[num+1] = tmp
                assorted = False

    return numbers

random_list = fill_list_with_randoms(min_bound,max_bound)
print("The list in the beginning : {}".format(random_list))
print("The list sorted: {}".format(bubble_sort(random_list)))



