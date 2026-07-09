import random

'''
Rock = -1 
Paper = 1 
Scissor = 0

'''

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice : ")
youdict = {"rock":-1 , "paper":1 , "scissor":0}
revdict = {-1:"rock", 1:"paper", 0:"scissor"}

you = youdict[youstr]

# by now we have 2 numbers (variables), you and computer
print(f"You Choose {revdict[you]} \n Computer Choose {revdict[computer]}")

if (computer == you):
    print("Its a Draw")

else:
    # if(computer ==-1 and you == 0): -1
    #     print("You lose")
    # elif(computer == 1 and you == -1): 2
    #     print("You lose")
    # elif(computer == 0 and you == 1): -1
    #     print("You lose")
    # elif(computer == -1 and you ==1): -2
    #     print("You Win")
    # elif(computer == 1 and you == 0): 1
    #     print("You Win")
    # elif(computer == 0 and you == -1): 1
    #     print("You Win")
    # else:
    #     print("Something Is Wrong")
    # the below logic is written on the basis of the value of computer - you 

    if((computer - you) == -2 or (computer - you) == 1 ):
        print("You Win")
    else:
        print("You Lose")