from const import freFile, probabilities, diffFactor

class Bot:
    def __init__(self, words):
        #Method1: self.fre = {}
        #self.loadStats()
        self.words = []
        self.resetWords(words)
    
    def resetWords(self, words):
        self.words = words
        self.sort_highest()
    
    def sort_highest(self):
        self.words = sorted(self.words, key=self.calculate_rank)
    
    def new_guess(self, old_word):
        self.words.remove(old_word)
        return self.guess()
    
    def guess(self):
        guess = self.words[-1]  
        return guess
   
    def filter(self, guess, hints):
        new_words = []
        cnt = {}
        for i in range(26):
            cnt[chr(ord('a')+i)] = 0
        for i in range(5):
            cnt[guess[i]] += 1
            if (hints[i] == "B"):
                cnt[guess[i]] -= 1
        
        for w in self.words:
            ok = 1
            for i in range(5):
                if ((hints[i] == "G" and w[i] != guess[i]) or
                    (hints[i] == "Y" and w[i] == guess[i]) or
                    (w.count(guess[i]) < cnt[guess[i]]) or
                    (cnt[guess[i]] == 0 and w.count(guess[i]) > 0)):
                    ok = 0
                    break

            if ok: new_words.append(w)

        self.words = new_words

    '''
    Method 1 is using probability of each letter appearing
    plus an additional factor that rewards words with multiple letters
    Avg: 3.8864229765013056, Fails: 136
    '''
    def calculate_rank(self, word):
        rank = 0
        for c in word.upper(): rank += probabilities[c]
        rank /= 5
        rank += diffFactor*len("".join(set(word)))
        return rank

    '''
    Method 2 was using frequency of letter at each position
    to rank the words

    Avg: 4.022499134648667, Fails: 311

        def loadStats(self):
        with open(freFile, "r") as file:
            for i, line in enumerate(file):
                self.fre[i] = {}
                for j, x in enumerate(line.split()):
                    self.fre[i][j] = int(x)

        def calculate_score(self, word):
            score = 0
            for j, c in enumerate(word):
                score += self.fre[ord(c)-ord('a')][j]
            return score
    '''