import time

from src.dp.dimension_2.a_min_cost_path import min_cost_path_dp_iter, min_cost_path_dp_memo, min_cost_path_recurs
from src.dp.dimension_2.b_lcs import lcs_dp_iter, lcs_dp_memo, lcs_recurs

def test_min_cost_path():

    test_cases = [
        {
            'input': [
                [5, 7, 2, 4],
                [1, 8, 1, 3],
                [6, 2, 9, 5],
                [1, 6, 2, 8]
            ],
            'output': 18
        },
        {
            'input': [
                [10, 6, 9, 0],
                [-23, 8, 9, 90],
                [-200, 0, 89, 200]
            ],
            'output': 76
        },
        {
            'input': [
                [9, 6, 0, 12, 90, 1],
                [2, 7, 8, 5, 78, 6],
                [1, 6, 0, 5, 10, -4],
                [9, 6, 2, -10, 7, 4],
                [10, -2, 0, 5, 5, 7]
            ],
            'output': 18
        },
        {
            'input': [
                [1,3,1],
                [1,5,1],
                [4,2,1]
            ],
            'output': 5
        }
    ]

    # Naive Approach
    start = time.time()
    for test_case in test_cases:
        matrix = test_case['input']
        assert test_case['output'] == min_cost_path_recurs(matrix, len(matrix), len(matrix[0]), 0, 0)
    end = time.time()
    print('Naive Approach', (end - start))

    # Memoization Approach
    start = time.time()
    for test_case in test_cases:

        matrix = test_case['input']
        dp_matrix = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        assert test_case['output'] == min_cost_path_dp_memo(matrix, len(matrix), len(matrix[0]), 0, 0, dp_matrix)
    end = time.time()
    print('Memoization Approach', (end - start))

    # Iteration Approach
    start = time.time()
    for test_case in test_cases:
        
        matrix = test_case['input']
        assert test_case['output'] == min_cost_path_dp_iter(matrix, len(matrix), len(matrix[0]))
    end = time.time()
    print('Iteration Approach', (end - start))

def test_lcs():

    test_cases = [
        {
            'input1': 'adebc',
            'input2': 'dcadb',
            'output': 3
        },
        {
            'input1': 'def',
            'input2': 'fed',
            'output': 1
        },
        {
            'input1': 'abcdb',
            'input2': 'bcacdhb',
            'output': 4
        },
        {
            'input1': 'abdgec',
            'input2': 'bfdmgjc',
            'output': 4
        }
    ]

    # Naive Approach
    start = time.time()
    
    for test_case in test_cases:
        s = test_case['input1']
        t = test_case['input2']
        
        assert test_case['output'] == lcs_recurs(s, t)
    
    end = time.time()
    print('Naive Approach', (end - start))

    # Memoization Approach
    start = time.time()
    
    for test_case in test_cases:

        s = test_case['input1']
        t = test_case['input2']
        matrix = [[-1 for j in range(len(t))]for i in range(len(s))]

        assert test_case['output'] == lcs_dp_memo(s, t, 0, 0, matrix)
    
    end = time.time()
    print('Memoization Approach', (end - start))

    # Iteration Approach
    start = time.time()
    
    for test_case in test_cases:
        
        s = test_case['input1']
        t = test_case['input2']
        
        assert test_case['output'] == lcs_dp_iter(s, t)
    
    end = time.time()
    print('Iteration Approach', (end - start))