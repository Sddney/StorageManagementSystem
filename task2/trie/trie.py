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

    def contains(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True

    def delete(self, word: str)-> bool:
        return self._inner_delete(self.root, word, 0)

    def _inner_delete(self, node, word, depth) -> bool:
        if depth == len(word):

            if not node.is_leaf:
                return False

            node.is_leaf = False

            return len(node.children) == 0

        char = word[depth]

        if char not in node.children:
            return False

        child = self._inner_delete(node.children[char], word, depth + 1)

        if child:
            del node.children[char]

            return not node.is_leaf and len(node.children) == 0

        return True



