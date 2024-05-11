from modes import OnePlayer, BotPlayer, BotCheat
from tools import loadWords

def main():
    type = int(input("Options:\n1. Player\n2. Bot\n3. Cheat\nChoose: "))
    print("\n")

    words = loadWords()

    if type == 1:
        OnePlayer(words)
    elif type == 2:
        BotPlayer(words)
    elif type == 3:
        BotCheat(words)
    
    print("\n")

if __name__ == "__main__":
    main()
