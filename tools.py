def loadWords(file):
    words = []
    with open(file, "r") as file:
        words = file.read().splitlines()
    return words

def calcProb(words):
    fre = dict()
    for i in range(26):
        fre[i] = 0

    tot = 0
    for s in words:
        for c in s:
            fre[ord(c)-ord('a')] += 1
        tot += 5

    for i in range(26):
        print(f"'{chr(i+ord('A'))}' : {int(10*(100*(fre[i]/tot)))/10},")

def calcFre(words, freFile):
    fre = dict()
    for i in range(26):
        fre[i] = dict()
        for j in range(5):
            fre[i][j] = 0

    for s in words:
        for i in range(5):
            fre[ord(s[i])-ord('a')][i] += 1
    
    with open(freFile, "w") as file:
        for i in range(26):
            for j in range(5):
                file.write(f"{fre[i][j]} ")
            file.write("\n")

def check(word, guess):
    hints = ["B", "B", "B", "B", "B"]
    rem = ""
    for i in range(5):
        if guess[i] == word[i]: hints[i] = "G"
        else: rem += word[i]
    for i in range(5):
        if hints[i] == "G": continue
        if guess[i] in rem:
            hints[i] = "Y"
            rem = rem.replace(guess[i], "", 1)
    return hints

def printCheck(guess, hints):
    for i in range(5):
        if hints[i] == "G":
            print(f"\033[1;32m{guess[i]}\033[0m", end='')
        elif hints[i] == "Y":
            print(f"\033[1;33m{guess[i]}\033[0m", end='')
        else:
            print(f"\033[1;30m{guess[i]}\033[0m", end='')
    
    print("\n", end='')
