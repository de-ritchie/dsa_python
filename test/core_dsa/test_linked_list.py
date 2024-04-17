from src.core_dsa.g_linked_list.a_reverse_linked_list import reverse_iter, reverse_recurs
from src.core_dsa.g_linked_list.b_k_reverse import reverse_k_group

from src.core_dsa.util.linked_list import array_to_linked_list, linked_list_to_array

def test_reverse_linked_list():

    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [i for i in range(11)],
        [i for i in range(50)]
    ]

    for test_case in test_cases:
        
        # Test Recursive Solution
        actual = reverse_recurs(array_to_linked_list(test_case))
        assert linked_list_to_array(actual) == test_case[::-1]

        # Test Iterative Solution
        actual = reverse_iter(array_to_linked_list(test_case))
        assert linked_list_to_array(actual) == test_case[::-1]

def test_k_reverse_linked_list():

    test_cases = [
        [i for i in range(7)],
        [i for i in range(8)],
        [i for i in range(9)]
    ]

    for test_case in test_cases:
        
        print(test_case)
        ll = array_to_linked_list(test_case)
        actual = reverse_k_group(ll, 3)
        print(linked_list_to_array(actual))