import random
import emoji

values = [1,2,3,4,5,6]
score = 0
wickets = 0
mic = emoji.emojize("\U0001F399")
bat = emoji.emojize("\U0001F3CF")

print("Hello")
name = input("Please enter your name: ")
print("Welcome, " , name)
print("Score 50 runs to win. You have 10 wickets. \nRuns allowed: 1 , 2 , 3 , 4 , 5 , 6 . \nIf the number you enter matches the generated number, then it would be OUT. Otherwise, you will earn runs.")

while wickets < 10 :
    if(score >= 50):
        print("Congratulations! You won! Your score is " , score , " / " , wickets)
        break
    pc_runs = random.choice(values)
    user_input = input("Play a shot: ")
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
            match user_runs:
                case 1:
                    print(mic , ": Gentle touch. Just one run.")
                case 2:
                    print(mic , ": Pushed to the cover, and the batters secure 2 runs.")
                case 3:
                    print(mic , ": Fast running! 3 runs.")
                case 4:
                    print(mic , ": Beautifully glanced for 4!")
                case 5:
                    print(mic , ": Over the keeper's head and it races away to the boundary! 5 wides!")
                case 6:
                    print(mic , ": That's a huge SIX!")
            #print("You score " , user_runs , " runs.")
            score = score + user_runs
            print("Your score: " , score , " / " , wickets , "\n")
    except ValueError:
        print("Not a number! \n")