from src.core_dsa.util.trees.trie import Trie

def test_trie_ds():

    test_cases = [
        {
            'words': ['apple', 'ape', 'mango', 'news', 'no'],
            'queries': ['apple', 'new', 'ape', 'not'],
            'output': [True, False, True, False]
        }
    ]

    for test_case in test_cases:
        
        trie = Trie()

        for word in test_case['words']:
            trie.insert(word)
        
        for i, query in enumerate(test_case['queries']):
            assert trie.search(query) == test_case['output'][i]