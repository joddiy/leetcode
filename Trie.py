class TrieNode(object):
    def __init__(self, x):
        self.val = x
        self.dict = [None] * 26
        
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
        curr_dict = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if curr_dict.dict[idx] is None:
                curr_dict.dict[idx] = TrieNode(False)
            curr_dict = curr_dict.dict[idx]
        curr_dict.val = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr_dict = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if curr_dict.dict[idx] is None:
                return False
            curr_dict = curr_dict.dict[idx]
        return curr_dict.val

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr_dict = self.root
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - ord('a')
            if curr_dict.dict[idx] is None:
                return False
            curr_dict = curr_dict.dict[idx]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app") 
trie.search("app")