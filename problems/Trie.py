from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.store = False
        self.next = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tmp = self.root
        for c in word:
            tmp = tmp.next[c]
        tmp.store = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmp = self.root
        for c in word:
            if c in tmp.next:
                tmp = tmp.next[c]
            else:
                return False
        return tmp.store


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.root
        for c in prefix:
            if c in tmp.next:
                tmp = tmp.next[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
