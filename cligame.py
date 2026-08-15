import random
target=random.randint(1,100)
guesses=0
guess=int(input("guess the number"))

while guess!=target:
    guesses+=1
    if guess==target:
        break
    elif guess>target:
        print("too high")    
    else:
        print("too low")
    
    guess=int(input("guess the number"))

print("you got it in ",guesses,"guesses")