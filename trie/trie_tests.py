import unittest
from trie.trie import Trie

class TestTrie(unittest.TestCase):
    def test_trie_insert(self):
        t = Trie()

        t.insert('apple')
        t.insert('application')


        assert t.contains('ap') == True and t.contains('appl') == True

    def test_trie_delete(self):
        t = Trie()

        t.insert('tea')
        t.delete('a')

        assert t.contains('a') == False and t.contains('te') == True
