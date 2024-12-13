# integer number
x = 2
print(x)
print(type(x))

#  floating number
y = 1.48
print(y)
print(type(y))

# complex number
z = 2+4j
print(z)
print(type(z))

# boolean
q = True
print(q)
print(type(q))

#string formatting
name = "Htoo Htoo Zaw"
age = 20
place = "UCSY"
print(f"I am {name}, I am {age} years old. I live in {place}")

print("I need a %s"%'grilfriend')
need = "boyfriend"
print('I need a %s'%need)
print('I need %d %s'%(2, 'boyfriends'))
print('I need a {}'.format(need))

# sequence data type
x = "Hello world"
print(x)
print(type(x))
print(x[:])
print(x[6])
print(x[6:])
print(x[:6])
print(x[6:8])
print(x[2:8:3])

# list which contains strings
students = ["Mg Mg", "Moe Moe", "Aung Aung", "Win Win"]
print(students)
print(type(students))

# list which contains integers
x = [1, 3, 2, 6, 7]
print(x)
print(type(x))

# list which contains different data type
y = ['Python', 12, 1.485, 1+5j]
print(y)
print(type(y))

# two dimensional list (list of lists)
x = [[1,2,3,4],[5,6,7,8]]
print(x)

# some parts are drawn from the list
y = [1,3,2,6,7]
print(y[3])

# some parts are drawn from the list of lists
x = [[1,2,3,4],[5,6,7,8]]
print(x[0])
print(x[0][1])

# len for counting set
# append for adding set to the last index of list

students = ["Thuzar", "Nandar", "Muyar", "Kyipyar"]
print(len(students))
print(students)
print(f"Before appending:{students}")

# using append
students.append("Ma Ma")

print(f"After appending:{students}")

# using extend
new_students = ["Aung Aung", "Kyaw Kyaw", "Mg Mg"]
students.extend(new_students)
print(students)

# using count
students = ["Thuzar", "Nandar", "Muyar", "Kyipyar", "Thuzar"]
number_of_students = students.count("Thuzar")

print(number_of_students)

# using pop
last_student = students.pop()
print(students)
print(last_student)

second_student = students.pop()
print(students)
print(second_student)

second_student = students.pop(1)
print(second_student)

# using insert
students.insert(0, "Ko Ko")
print(students)

# using index
test = students.index("Muyar")
print(test)

"""
# integer number
x = 2
print(x)
print(type(x))

#  floating number
y = 1.48
print(y)
print(type(y))

# complex number
z = 2+4j
print(z)
print(type(z))

# boolean
q = True
print(q)
print(type(q))

#string formatting
name = "Htoo Htoo Zaw"
age = 20
place = "UCSY"
print(f"I am {name}, I am {age} years old. I live in {place}")

print("I need a %s"%'grilfriend')
need = "boyfriend"
print('I need a %s'%need)
print('I need %d %s'%(2, 'boyfriends'))
print('I need a {}'.format(need))

# sequence data type
x = "Hello world"
print(x)
print(type(x))
print(x[:])
print(x[6])
print(x[6:])
print(x[:6])
print(x[6:8])
print(x[2:8:3])

# list which contains strings
students = ["Mg Mg", "Moe Moe", "Aung Aung", "Win Win"]
print(students)
print(type(students))

# list which contains integers
x = [1, 3, 2, 6, 7]
print(x)
print(type(x))

# list which contains different data type
y = ['Python', 12, 1.485, 1+5j]
print(y)
print(type(y))

# two dimensional list (list of lists)
x = [[1,2,3,4],[5,6,7,8]]
print(x)

# some parts are drawn from the list
y = [1,3,2,6,7]
print(y[3])

# some parts are drawn from the list of lists
x = [[1,2,3,4],[5,6,7,8]]
print(x[0])
print(x[0][1])

# len for counting set
# append for adding set to the last index of list

students = ["Thuzar", "Nandar", "Muyar", "Kyipyar"]
print(len(students))
print(students)
print(f"Before appending:{students}")

# using append
students.append("Ma Ma")

print(f"After appending:{students}")

# using extend
new_students = ["Aung Aung", "Kyaw Kyaw", "Mg Mg"]
students.extend(new_students)
print(students)

# using count
students = ["Thuzar", "Nandar", "Muyar", "Kyipyar", "Thuzar"]
number_of_students = students.count("Thuzar")

print(number_of_students)

# using pop
last_student = students.pop()
print(students)
print(last_student)

second_student = students.pop()
print(students)
print(second_student)

second_student = students.pop(1)
print(second_student)

# using insert
students.insert(0, "Ko Ko")
print(students)

# using index
test = students.index("Muyar")
print(test)

"""
