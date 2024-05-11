from probabilities import probabilities

class Bot:
    def __init__(self, words):
        self.words = words
    
    def guess(self):
        guess = ""
        highest_p = 0

        for w in self.words:
            p = self.calculate_probability(w)
            if p > highest_p:
                guess = w
                highest_p = p
        
        return guess

    def filter(self, guess, hints):
        new_words = []
        for i in range(len(self.words)):
            word = self.words[i]
            
            isValid = True
            for j in range(5):
                # Filter green
                if hints[j] == "G" and guess[j] != word[j]:
                    isValid = False
                    break

                # Filter yellow
                if hints[j] == "Y" and (guess[j] == word[j] or word.count(guess[j]) == 0):
                    isValid = False
                    break

                # Filter black
                if hints[j] == "B":
                    indexes = [pos for pos, char in enumerate(guess) if char == guess[j]]

                    occurences = len(indexes)
                    for h in indexes:
                        if hints[h] == "B":
                            occurences -= 1
                    
                    if word.count(guess[j]) != occurences:
                        isValid = False
                        break

            
            if isValid:
                new_words.append(word)
        
        self.words = new_words


    def calculate_probability(self, word : str):
        probability : int = 1
        for c in word.upper():
            probability *= probabilities[c]
        return probability