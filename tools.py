import colorama

def loadWords():
    words = []
    with open("valid-wordle-words.txt", "r") as file:
        words = file.read().splitlines()
    return words

def check(word, guess):
    hints = []
    checked = []
    for i in range(5):
        if guess[i] == word[i]:
            hints.append("G")
            if i in checked:
                for j in range(i):
                    if guess[j] == guess[i]:
                        hints[j] = "B"
                        break

            checked.append(i)
        elif guess[i] in word and word.index(guess[i]) not in checked:
            hints.append("Y")
            checked.append(word.index(guess[i]))
        else:
            hints.append("B")
    return hints

def printCheck(guess, hints):
    for i in range(5):
        if hints[i] == "G":
            print(colorama.Back.GREEN + guess[i], end='')
        elif hints[i] == "Y":
            print(colorama.Back.YELLOW + guess[i], end='')
        else:
            print(colorama.Back.BLACK + guess[i], end='')
    
    print(colorama.Style.RESET_ALL, end="\n")