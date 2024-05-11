from random import choice
from tools import check, printCheck
from bot import Bot

def OnePlayer(words):
    word = ""
    with open("COMMON_WORDS.txt", "r") as file:
        word = choice(file.read().splitlines())
    
    print("6 tries to guess a 5-letter word")
    
    for i in range(6):
        guess = ""

        while guess not in words:
            guess = input()
            print("\033[1A[\033[2K", end="\b") # Erase last input
        
        hints = check(word, guess)
        printCheck(guess, hints)

        if hints == ["G", "G", "G", "G", "G"]:
            print("You win!")
            return
    
    print(f"The word was {word}")

def BotPlayer(words):
    bot = Bot(words)
    
    print("Input the colours after each guess (G = green, Y = yellow, B = black)")
    print("Example: GGYBY\n")

    for i in range(6):
        guess = bot.guess()
        
        print(guess)
        hints = list(map(str, input()))
        
        print("\033[1A[\033[2K", end="\b")
        print("\033[1A[\033[2K", end="\b")
        printCheck(guess, hints)

        if hints == ["G", "G", "G", "G", "G"]:
            if i == 0:
                print("The bot guessed your word in 1 try")
            else:
                print(f"The bot guessed your word in {i+1} tries")
            return
        
        bot.filter(guess, hints)

    print(f'The bot could not guess tiyr wird in 6 tries or less')

