print("Welcome to my compuetr quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":    # to lowercase all the letters
    quit()

print("Okay! Let's Play")
score = 0
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("Wrong")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("Wrong")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("Wrong")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("correct")
    score += 1
else:
    print("Wrong")

print("You got "+ str(score) + " questions correct!")
print("You got "+ str((score/4)*100) + "%.")