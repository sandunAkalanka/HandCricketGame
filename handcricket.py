import random
values = [1,2,3,4,5,6]
score = 0
wickets = 0
print("Hello")
name = input("Please enter your name: ")
print("Welcome, " , name)
print("core 50 runs to win. You have 10 wickets. \nRuns allowed: 1 , 2 , 3 , 4 , 5 , 6 . \nIf the number you enter matches the generated number, then it would be OUT. Otherwise, you will earn runs.")

while wickets < 10 :
    if(score >= 50):
        print("Congratulations! You won! Your score is " , score , " / " , wickets)
        break
    pc_runs = random.choice(values)
    user_input = input("Offer a shot: ")
    try:
        user_runs = int(user_input)
        if user_runs < 1 or user_runs > 6:
            print("Please enter a number between 1 and 6 \n")
            continue
        print("PC says: " , pc_runs)
        if (pc_runs == user_runs):    
            print("You entered the same number as PC. You are OUT!")
            wickets += 1
            print("Your score: " , score , " / " , wickets , "\n")
        else:
            print("You score " , user_runs , " runs.")
            score = score + user_runs
            print("Your score: " , score , " / " , wickets , "\n")
    except ValueError:
        print("Not a number! \n")