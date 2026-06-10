'''
# this is my first python program.
print("I like rolls.");
print("It's really good.");


# variables = A container for a value (String, integer, float, boolean)
# A variable behaves as if it was the value it contains

# Strings
first_name = "Yehan" 
food = "Rolls"
email = "yehan@gmail.com"

print(f"hello {first_name}")
print(f"You like {food}.");
print(f"Your email is {email}");


# Integers
age = 20
quantity = 3
number_if_students = 25

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {number_if_students} students.")

#Float
price = 10.99
gpa = 3.2
distance = 3.0

print(f"The price is ${price}.")
print(f"My GPA is {gpa}")
print(f"You ran {distance}km.")

# Boolean
is_student = True
#print(f"Are you a student? {is_student}")
if is_student:
    print("You are a student")
else:
    print("You are not a student")

for_sale = True

if for_sale:
    print("This is for sale")
else:
    print("This is not for sale.")

is_online = False

if is_online:
    print("You are online")
else:
    print("You are offline")

# Typecasting = the process of converting variable's data type from one to another 
#               str(), int(), float(), bool()

name = "Yehan"
age = 20
gpa = 3.5
is_student = True

print(type(name))   # string
print(type(age))    # integer  
print(type(gpa))    # float
print(type(is_student)) # boolean

gpa = int(gpa)
print(f"GPA - {gpa}")

print(type(gpa))

age = float(age)
print(age)
print(f"Age: {age} and Type:{type(age)}") # 20.0 , float
age = str(age)  
print(age)  #20.0   
print(type(age))    # str

print(bool(name))  #True
name = ""
print(bool(name)) #False

# input() = this is a function that user to enter data by user as string

name = input("What is your name?: ")
age = input("How old are you?: ")

print(f"Hello {name}")
print("HAPPY BIRTHDAY !!!")
print(f"You are {age} years old.")

# method 1
age = int(age)
age += 1
print(age)

# method 2
age = int(input("Enter your age: "))

'''

# Exercise 1 - rectangle area calc

length = float(input("Enter the length(cm): "))
width = float(input("Enter the width(cm): "))
area = length * width
print(f"Area of rectangle is {area} cm².")