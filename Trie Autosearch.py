"""
TRIE DATA STRUCTURE

https://leetcode.com/discuss/general-discussion/931977/beginner-friendly-guide-to-trie-tutorial-practice-problems

Trie is a popular data structure to store and process strings.
Trie is a rooted tree that stores a set of strings. Each string starts at the root, and each edge in the tree represents a single character.

"""


# A class that represents an nodes of an Trie
class TrieNode():
    def __init__(self):
       self.children = {}
       self.isEndOfWord = False # isEndOfWord is True if node represent the end of the word 


# A class that reprsents an actual Trie
class Trie:
    def __init__(self):
        self.root = self.getNode()
        self.wordList = []

    # initializes the Trie Node
    def getNode(self):
        return TrieNode()

    # private helper function to return char to index value 
    def _charToIndex(self, char):
        return ord(char) - ord('a')

    # inserts new word in the trie structure
    def insert(self, word):
        pCrawl = self.root
        for char in word:
            # index = self._charToIndex(char)
            if not pCrawl.children.get(char, False):
                pCrawl.children[char] = self.getNode()
            pCrawl = pCrawl.children[char]
        pCrawl.isEndOfWord = True

    # searches for given word in a trie
    def search(self, word):
        pCrawl = self.root
        for char in word:
            # index = self._charToIndex(char)
            if not pCrawl.children.get(char, False):
                return False
            pCrawl = pCrawl.children[char]
        return True

    # helper function to find relatedWords
    def suggestionsRec(self, node, tempWord):
        if node.isEndOfWord:
            self.wordList.append(tempWord)

        for char, newNode in node.children.items():
            self.suggestionsRec(newNode, tempWord+char)

    # actual function to return words that starts with given text, used for autosuggestions
    def relatedWords(self, text):
        pCrawl = self.root
        tempWord = ""
        for char in text:
            if not pCrawl.children.get(char, False):
                return 0
            tempWord += char
            pCrawl = pCrawl.children[char]
        if pCrawl.isEndOfWord and not pCrawl.children:
            return -1

        self.suggestionsRec(pCrawl, tempWord) 
        for word in self.wordList:
            print(word)
        return 1

if __name__ == "__main__":
    words = int(input("Enter the number of words: "))
    listOfWords = []
    tree = Trie()
    while words > 0:
        word = input("Enter the word: ")
        listOfWords.append(word)
        tree.insert(word)
        words -= 1

    text = input("Enter the word to search for: ")
    # if tree.search(text):
        # print("Word Found.")
    # else:
        # print("Word not Found.")

    resp = tree.relatedWords(text)
    if resp == -1:
        print("No other strings found with this prefix\n")
    elif resp == 0:
        print("No string found with this prefix\n") 


