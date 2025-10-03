from random import choice
from tools import check, printCheck
from bot import Bot

def OnePlayer(words):
    word = choice(words)
    
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
    print("Example: GGYBY")
    print('Input "change" to change guess\n')

    for i in range(6):
        guess = bot.guess()
        
        print(guess)
        hints = input()
        
        while hints == "change":
            print("\033[1A[\033[2K", end="\b")
            print("\033[1A[\033[2K", end="\b")
            guess = bot.new_guess(guess)
            print(guess)
            hints = input()
        
        hints = list(map(str, hints))
        
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

    print(f'The bot could not guess the word in 6 tries or less')

def simulate(words):
    sum, cnt = 0, 0
    fails = []
    for w in words:
        bot = Bot(words)
        ok = 0
        for i in range(6):
            guess = bot.guess()
            hints = check(w, guess)
            if hints == ["G", "G", "G", "G", "G"]:
                sum += i+1
                cnt += 1
                ok = 1
                break
            bot.filter(guess, hints)
        if (not ok):
            fails.append(w)

    print(f"Avg: {(100*(sum/cnt))/100}, Fails: {len(fails)}")
    with open("failed_words.txt", "w") as file:
        for f in fails:
            file.write(f"{f}\n")