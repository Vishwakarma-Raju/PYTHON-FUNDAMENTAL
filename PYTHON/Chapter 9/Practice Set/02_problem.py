import random


def game():
    print("You are playing game.. ")
    score = random.randint(1,100)

# fetch the Hiscore

    with open("Hiscore.txt") as f:
        Hiscore = f.read()
        if( Hiscore !=""):
            Hiscore = int(Hiscore)
        else:
            Hiscore = 0

        print(f"Your Score is : {score}")
        if(score>Hiscore):
            with open("Hiscore.txt", "w") as f:
                f.write(str(score))
    
        return score
    
game()