class TrieNode:
    ALPHABET_SIZE = 29 # add 2 [' , - , '/']

    def __init__(self):
        self.children = TrieNode.ALPHABET_SIZE * [None]
        self.is_end_of_word = False


class Trie:

    SPECIAL_SYMBOLS = ['\'', '-', '/']

    @staticmethod
    def create_trie(dictionary: list):
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        return trie


    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        size = len(key)
        print(key)

        for level in range(size):
            index = Trie._get_index_of_char(key[level])

            if not current.children[index]:
                current.children[index] = TrieNode()

            current = current.children[index]

        current.is_end_of_word = True


    def search(self, key):
        current = self.root
        size = len(key)

        for level in range(size):
            index = self._get_index_of_char(key[level])

            if index < 0 or index >= len(current.children):
                return False

            if not current.children[index]:
                return False

            current = current.children[index]

        if current is None:
            return False

        return current.is_end_of_word

    @staticmethod
    def _get_index_of_char(symbol) -> int:
        if symbol in Trie.SPECIAL_SYMBOLS:
            return 26 + Trie.SPECIAL_SYMBOLS.index(symbol)

        index = ord(symbol) - ord('a')
        return index





