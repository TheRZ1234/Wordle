from modes import OnePlayer, BotPlayer
from tools import loadWords
from colorama import Style

def main():
    print(Style.RESET_ALL)
    type = int(input("\nOptions:\n1. Player\n2. Bot\nChoose: "))
    print("\n")

    words = loadWords()

    if type == 1:
        OnePlayer(words)
    elif type == 2:
        BotPlayer(words)
    
    print("\n")

if __name__ == "__main__":
    main()
