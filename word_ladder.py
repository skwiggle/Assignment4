import re
#Created class WordLadder to be called upon later on
class WordLadder:
#added self to all methods inside the created class
    def start(self, fname, start, target):
        #Commented out the input to allow for automated testing in bottom of code
        # fname = input("Enter dictionary name: ")

        file = open(fname)
        lines = file.readlines()
        while True:
            # Commented out the input to allow for automated testing in bottom of code
            # start = input("Enter start word:")
            words = []
            for line in lines:
                word = line.rstrip()
                if len(word) == len(start):
                    words.append(word)

            #commented out to help with testing
            #target = input("Enter target word:")
            #added middle variable to help with extra required function
            middle=input("Enter middle word:")


            break
        path = [start]
        seen = {start: True}

        file.close()

        #added middle clause to add a middle word
        if middle != "":
            if self.find(start, words, seen, middle, path):
                path.append(middle)
                if self.find(middle, words, seen, target, path):
                    path.append(target)
                    return len(path) - 1, path
                #added previous clause made to dictate shortest distance from code below
                else:
                    print("No path found")
            else:
                print("No path found")

        if self.find(start, words, seen, target, path):
            path.append(target)
            return (len(path) - 1, path)

        else:
            if self.find(start, words, seen, target, path):
                path.append(target)
                return len(path) - 1, path
            else:
                print("No path found")

    def same(self, item, target):
        return len([c for (c, t) in zip(item, target) if c == t])

    def build(self, pattern, words, seen, item_list):
        return [word for word in words
                if re.search(pattern, word) and word not in seen.keys() and
                word not in item_list]

    def find(self, word, words, seen, target, path):
        #added matchingletters variable
        matchingletters = []
        #renamed list to item_list to avoid confusion
        item_list = []
        #inserted logic for shortening distance between word and target
        if (sum(1 for (c, t) in zip(word, target) if c == t)) > 0:
            matchingletters = [i for i, x in enumerate(zip(word, target)) if all(y == x[0] for y in x)]
        for i in range(len(word)):
            if i not in matchingletters:
                item_list += self.build(word[:i] + "." + word[i + 1:], words, seen, item_list)
        if len(item_list) == 0:
            return False
        item_list = sorted([(self.same(w, target), w) for w in item_list], reverse=True)
        #above code allows the word to get to the target as soon as possible rather than exhausting every outcome as seen prior
        for (match, item) in item_list:
            if match >= len(target) - 1:
                if match == len(target) - 1:
                    path.append(item)
                return True
            seen[item] = True
        for (match, item) in item_list:
            path.append(item)
            if self.find(item, words, seen, target, path):
                return True
            path.pop()

word_game = WordLadder()
#used for correct acceptance testing
print(word_game.start("dictionary.txt", "lead", "gold"))

