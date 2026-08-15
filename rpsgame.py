import random
choice=['rock','paper','scissor']
urchoice=input("enter your choice: ")
compchoice=random.choice(choice) 
beat={'rock':'scissor','paper':'rock','scissor':'paper'}
if urchoice==compchoice:
    print("tie")
elif beat[urchoice]==compchoice:
    print("user wins")
else:
    print("computer wins")
    print("computer choose",compchoice)