from const import probabilities, diffFactor

class Bot:
    def __init__(self, words):
        self.words = words
        #self.FIRST_GUESS = "slate"
        
        self.sort_highest()
    
    def sort_highest(self):
        self.words = sorted(self.words, key=self.calculate_rank)
        
       # self.words.remove(self.FIRST_GUESS)
       # self.words.append(self.FIRST_GUESS)
    
    def new_guess(self, old_word):
        self.words.remove(old_word)
        return self.guess()
    
    def guess(self):
        guess = self.words[-1]  
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


    def calculate_rank(self, word):
        rank = 0
        for c in word.upper(): rank += probabilities[c]
        rank /= 5
        rank += diffFactor*len("".join(set(word)))
        return rank