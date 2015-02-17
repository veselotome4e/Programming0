def square(n):
    return n**2

#print(square(2))
#print(square(5))

def fact(n):
    if n == 0:
        return 1
    else:
        start = 1
        fact = 1
        while start <=n:
            fact *= start
            start+=1
        return fact

#print(fact(5))
#print(fact(0))
#print(fact(6))

def count_elements(items):
    counter = 0
    for each in items:
        counter +=1
    return counter

#print(count_elements([]))
#print(count_elements([1,2,3]))

def member(n,items):
    if n in items:
        return True
    else:
        return False

#print(member(1,[1,2,3]))
#print(member("Python",["Djnago","Rails"]))

def grades_that_pass(students,grades,limit):
    passing_students = []
    index = 0
    for each_grade in grades:
        if each_grade >= limit:
            passing_students.append(students[index])
        index+=1
    return passing_students

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]
result = grades_that_pass(students,grades,4.0)
print(result)
