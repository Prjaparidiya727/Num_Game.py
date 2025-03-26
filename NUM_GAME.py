import random
positive_score=0
negative_score=0

def play_game(user_num):
    global positive_score,negative_score
    random_num=random.randint(1,5)
    print(f"Random num={random_num}")
    if user_num==random_num:
        positive_score +=1
        print(f" COngratulation U Win, positive score Increse {positive_score}")
    else:
        negative_score +=1
        print(f"U Loss, Negative score Increase {negative_score}")

while True:
    user_input=input("Enter from |1 to 5|, Press Q for Quite=")
    if user_input.upper()=='Q':
        print("By, Game Over")
        break
    
    user_num=int(user_input)
    if user_num>=1 and user_num<=5:
        play_game(user_num)
        print(f"This is your final Positive score={positive_score} and negative score={negative_score}")
    else:
        print("Write num in range of 1 to 5")
        
    
    
    
        
        