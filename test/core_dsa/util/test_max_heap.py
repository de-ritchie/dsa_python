from src.core_dsa.util.trees.max_heap import MaxHeap

def test_max_heap():

    test_cases = [
        {
            'ip': [11, 12, 3, 18, 14, 7, 18, 29, 42],
            'op': [42, 29, 18, 18, 12, 3, 7, 11, 14]
        }
    ]

    for test_case in test_cases:

        max_heap = MaxHeap(test_case['ip'])
        print(max_heap.heap)
        
        for num in sorted(test_case['ip'], reverse=True):
            assert max_heap.extract_max() == num

        max_heap = MaxHeap(test_case['ip'])

        assert max_heap.heap_sort() == sorted(test_case['ip'])