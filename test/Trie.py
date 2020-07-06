class TrieNode():

    def __init__(self, val):
        self.next = [None] * 26
        self.val = val


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(False)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not node.next[idx]:
                node.next[idx] = TrieNode(False)
            node = node.next[idx]
        node.val = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not node.next[idx]:
                return False
            node = node.next[idx]
        return node.val

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if not node.next[idx]:
                return False
            node = node.next[idx]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
