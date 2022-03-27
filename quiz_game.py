print("Welcome to gaming quiz!")

playing = input("Dp you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0

answer = input("What does PUBG stands for ? ")
if answer.lower() == "playerUnknown's battlegrounds":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")


answer = input("What does COC stands for ? ")
if answer.lower() == "clash of clan":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")


answer = input("What does COD Stands for ? ")
if answer.lower() == "call of duty":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")


answer = input("what does CS-GO stands for ? ")
if answer.lower() == "counter strike global offensive":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct.")
print(f"You got {(score/4)*100} $(precentage) marks.")