class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:

            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()

            curr_node = curr_node.children[char]

        curr_node.is_leaf = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True

    def starts_with(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True