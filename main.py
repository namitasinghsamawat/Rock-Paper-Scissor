
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
    if(computer==-1 and you ==0): # -1
        print("you win!")
    elif(computer==-1 and you==1): # -2
        print("you lose")
    elif(computer==0 and you==1): # -1
        print("you win!")
    elif(computer==0 and you==-1): # 1
        print("you lose")
    elif(computer==1 and you==-1): # 2
        print("you win")
    elif(computer==1 and you==0): # 1
        print("you lose")
    else:
        print("something went wrong")





