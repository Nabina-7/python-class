import random
computer_score=0
user_score=0
for x in range(0,6,1):
    user_guess=int(input("Enter a guess number"))
    computer_guess=random.randint(0,6)
    print(computer_guess)
    if user_guess>computer_guess:
        user_score+=10
        print("user score is: " +str(user_score))
    elif user_guess<computer_guess:
        computer_score+=10
        print("computer score is:" +str(computer_score))
    else:
        user_score-=5
        computer_score-=5
        print("user score is:" +str(user_score))
        print("computer score is:" +str(computer_score))

