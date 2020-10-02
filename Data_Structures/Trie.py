class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        :param word: word to add.
        :return: None
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = dict()
            node = node[ch]
        node["*"] = None

    def search(self, word: str) -> bool:
        """
        :param word: word to check
        :return: if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "*" in node

    def startsWith(self, prefix: str) -> bool:
        """
        :param prefix: prefix to check
        :return: if there is any word in the trie that starts with the
        given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
