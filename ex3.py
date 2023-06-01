print("wel come to coputer quis")
playing = input("Do you wnat play ")
if playing .lower() !="yes":
    quit()

print("Okay! Let's play :")
score=0
answer = input("What does CPU stands for ")
if answer == "central processing unit":
    print('correct!')
    score +=1
else:
    print('incorrect!')
    
answer = input("What does GPU stands for ")
if answer == "graphics processing unit":
    print('correct!')
    score +=1
else:
    print('incorrect!')
    
answer = input("What does RAM stands for ")
if answer == "random access memory":
    print('correct!')
    score +=1
else:
    print('incorrect!')
    
answer = input("What does psu stands for ")
if answer.lower() == "power supply":
    print('correct!')
    score +=1
else:
    print('incorrect!')
    
answer = input("What does ROM stands for ")
if answer == "read only memory":
    print('correct!')
    score +=1
else:
    print('incorrect!')
    
print("You got " + str(score) + "question correct!")
print("You got " + str((score / 4) + 100) + "%.")


