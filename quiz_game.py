print("Welcome to gaming quiz!")

playing = input("Dp you want to play? ")

if playing.lower() != "yes":
    quit()

answer = input("What does PUBG stands for ? ")
if answer.lower() == "playerUnknown's battlegrounds":
    print("Correct! ")
else:
    print("Incorrect!")


answer = input("What does COC stands for ? ")
if answer.lower() == "clash of clan":
    print("Correct! ")
else:
    print("Incorrect!")


answer = input("What does COD Stands for ? ")
if answer.lower() == "call of duty":
    print("Correct! ")
else:
    print("Incorrect!")


answer = input("what does CS-GO stands for ? ")
if answer.lower() == "counter strike global offensive":
    print("Correct! ")
else:
    print("Incorrect!")

