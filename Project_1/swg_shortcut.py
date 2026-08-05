import random
computer= random.choice([1,-1,0])
youstr=input("Enter your choice :")
youDict={"s":1, "w":-1, "g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you= youDict[youstr]

print(f"You Choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")

'''
    if(computer ==-1 and you == 1): (computer - you) = -2
    print ("You win!")

    elif(computer ==-1 and you == 0): (computer - you) -1
    print ("You Lose!")

    elif(computer == 1 and you == -1): (computer - you) 2
    print ("You lose!")

    elif(computer ==1 and you == 0): (computer - you) 1
    print("You Win!")

    elif(computer == and you == -1): (computer - you) 1
    print ("You Win!")

    elif(computer == 0 and you == 1): computer - you)-1
    print("You Lose!")
'''
# The below logic is written on the basis of the value of computer - you
if computer == you:
    print("Draw!")

else:
    if (computer - you) == -1 or (computer - you) == 2:
        print("You Lose!")
    else:
        print("You Win!")