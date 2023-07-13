import random
computer_score=0
user_score=0
for x in range(1,6,1):
    user_guess=int(input("Enter a guess number"))
    computer_guess=random.randint(0,6)
    print(computer_guess)
if user_guess>computer_guess:
    print("user_guess+=5")
elif user_guess<computer_guess:
    print("computer_guess+=5")
else:
    print("No increament of point")
