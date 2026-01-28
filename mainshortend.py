
'''
-1 = rock
0 = paper
1 = scissor 

'''

import random
computer=random.choice([-1,0,1])

youstr=input("enter your chocice:")

youDict={"r":-1,"p":0,"s":1}
revdict={-1:"rock",0:"paper",1:"scissor"}

you = youDict[youstr]
print(f"your choice:{revdict[you]}\n computer's choice:{revdict[computer]}")

if(computer==you):
    print("it's a draw")
else:
    if((computer - you == 1) or (computer - you == -2)):
        print("you lose")
    else:
        print("you win")