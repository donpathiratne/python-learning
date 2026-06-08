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

'''

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
