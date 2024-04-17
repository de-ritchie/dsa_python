from typing import Dict

class TrieNode:

    def __init__(self, character: str) -> None:
        
        self.character: str = character
        self.is_terminal: bool = False
        self.children: Dict[str, TrieNode] = {}

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode(None)

    def insert(self, word: str):

        tmp = self.root

        for c in word:

            if tmp.children.get(c, None) is None:
                node = TrieNode(c)
                tmp.children[c] = node
            
            tmp = tmp.children[c]
        
        tmp.is_terminal = True
    
    def search(self, word: str):

        tmp = self.root

        for c in word:
            
            if tmp.children.get(c, None) is None:
                return False
            
            tmp = tmp.children[c]
        
        return tmp.is_terminal
