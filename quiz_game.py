print("Welcome to my compuetr quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's Play")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct")
else:
    print("Wrong")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("correct")
else:
    print("Wrong")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("correct")
else:
    print("Wrong")

answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print("correct")
else:
    print("Wrong")