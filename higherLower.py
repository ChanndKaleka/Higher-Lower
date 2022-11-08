from random import choice
from gameData import data
from random import choice
from art import logo, vs
from replit import clear

def formatData(account):
    accountName=account["name"]
    accountDescription=account["description"]
    return(f"{accountName} is a(n) {accountDescription}")

def checkAnswer(guess, firstFollowers, secondFollowers):
    if firstFollowers>secondFollowers:
        return guess=="a"
    else:
        return guess=="b"
    
score=0
gameOver=True
print(logo)
while gameOver==True:
    accountFirst=choice(data)
    accountSecond=choice(data)

    print(f"A: {formatData(accountFirst)}")
    print(vs)
    print(f"B: {formatData(accountSecond)}")

    guess=input("Type A or B: ").lower()

    firstFollowerCount=accountFirst["follower_count"]
    secondFollowerCount=accountSecond["follower_count"]

    isCorrect=checkAnswer(guess, firstFollowerCount,secondFollowerCount)

    if isCorrect:
        score+=1
        clear()
        print(f"You are right!\n The  current score is {score}")
        
    else:
        print("You are wrong!")
        gameOver=False