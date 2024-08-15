"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
otherwise. boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the
prefix prefix, and false otherwise.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.cur_node = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.cur_node
        for l in word:
            if l not in cur.children:
                cur.children.update({l: TrieNode()})
            cur = cur.children[l]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.cur_node
        for l in word:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return True if cur.is_end_of_word else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.cur_node
        for l in prefix:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return True