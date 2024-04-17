from src.core_dsa.util.trees.binary_tree import build_binary_tree, level_order_traversal

def test_level_order():

    test_cases = [
        {
            'ip': [1, 2, 3, 4, 5, None, 6, None, None, 7, None, None, None, None, None], 
            'op': [[1], [2, 3], [4, 5, 6], [7]]
        },
        {
            'ip': [3, 9, 20, None, None, 15, 7], 
            'op': [[3],[9,20],[15,7]]
        },
        {
            'ip': [], 
            'op': []
        }
    ]
    
    for test_case in test_cases:
        root = build_binary_tree(test_case['ip'])
        actual = level_order_traversal(root)

        print(actual)

        assert test_case['op'] == actual
