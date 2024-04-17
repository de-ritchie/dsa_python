from src.core_dsa.util.trees.binary_tree import level_order_traversal
from src.core_dsa.util.trees.binary_search_tree import sorted_array_to_bst

def test_sorted_array_to_bst():

    test_cases = [
        {
            'ip': [-10, -3, 0, 5, 9],
            'op': [[0], [-10, 5], [-3, 9]]
        },
        {
            'ip': [1, 3],
            'op': [[1], [3]]
        }
    ]

    for test_case in test_cases:

        root = sorted_array_to_bst(test_case['ip'])
        actual = level_order_traversal(root)
        print(actual)
        assert actual == test_case['op']