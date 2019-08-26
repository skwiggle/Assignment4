import re


class WordLadder:

    def start(self):
        fname = input("Enter dictionary name: ")
        file = open(fname)
        lines = file.readlines()
        while True:
            start = input("Enter start word:")
            words = []
            for line in lines:
                word = line.rstrip()
                if len(word) == len(start):
                    words.append(word)
            target = input("Enter target word:")
            break

        path = [start]
        seen = {start: True}
        if self.find(start, words, seen, target, path):
            path.append(target)
            print(len(path) - 1, path)
        else:
            print("No path found")

    def same(self, item, target):
        return len([c for (c, t) in zip(item, target) if c == t])

    def build(self, pattern, words, seen, item_list):
        return [word for word in words
                if re.search(pattern, word) and word not in seen.keys() and
                word not in item_list]

    def find(self, word, words, seen, target, path):
        item_list = []
        for i in range(len(word)):
            item_list += self.build(word[:i] + "." + word[i + 1:], words, seen, item_list)
        if len(item_list) == 0:
            return False
        item_list = sorted([(self.same(w, target), w) for w in item_list])
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
word_game.start()

