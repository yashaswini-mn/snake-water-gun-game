'''
1 for snake
-1 for water
0 for gun
'''

import random
computer= random.choice([1, 0, -1])

you = (input("enter your choice\n"))
youDict={
    "snake":1,
    "water": -1,
    "gun": 0
}
revyouDict={
    1:"snake",
    -1 :"water",
    0 :"gun"
}
you = youDict[you]

print(f"you chose {revyouDict[you]}\nYour computer chose {revyouDict[computer]}")

if (computer == you):
    print("It's a Draw")
else:
    if(computer == -1 and you == 1):
        print("You Win..!")
    
    elif(computer == -1 and you == 0):
        print("You lose..!")
    
    elif(computer == 1 and you == -1):
        print("You lose..!")
    
    elif(computer == 1 and you == 0):
        print("You win..!")
    
    elif(computer == 0 and you == -1):
        print("You Win..!")
    
    elif(computer == 0 and you == 1):
        print("You lose..!")
    
    else:
        print("Something went wrong")