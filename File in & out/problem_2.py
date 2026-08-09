import random

def game():
    score=random.randint(1,50)
    # Fetch the hiscore
    with open("HighScore.txt") as f:
        HiScore=f.read()
        if(HiScore!=""):
            HiScore=int(HiScore)
        else:
            HiScore=0

    print(f"your score is {score}")
    if(score>HiScore):
        with open("HighScore.txt","w") as f:
            f.write(str(score)) 

    return score

game()