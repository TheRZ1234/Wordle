from modes import OnePlayer, BotPlayer, simulate
from tools import loadWords, calc
from const import wordsFile

def main():
    type = int(input("\nOptions:\n1. Player\n2. Bot\n3. Simulate\n4. Calculate\nChoose: "))
    print("\n")

    words = loadWords(wordsFile)

    if type == 1:
        OnePlayer(words)
    elif type == 2:
        BotPlayer(words)
    elif type == 3:
        simulate(words)
    elif type == 4:
        calc(words)
    
    print("\n")

if __name__ == "__main__":
    main()