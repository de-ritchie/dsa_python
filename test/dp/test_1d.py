import time

from src.dp.dimension_1.a_staircase import staircase
from src.dp.dimension_1.b_min_steps import count_min_steps_to_one
from src.dp.dimension_1.c_min_num_squares import min_count
from src.dp.dimension_1.d_byte_landian import bytelandian, bytelandian_dp, bytelandian_recurs
from src.dp.dimension_1.e_loot import max_loot_dp_iter, max_loot_dp_mem, max_loot_recurs

def test_staircase():

    actual = staircase(4)
    assert actual == 7

    actual = staircase(10)
    assert actual == 274

def test_count_min_steps_to_one():

    actual = count_min_steps_to_one(4)
    assert actual == 2

    actual = count_min_steps_to_one(7)
    assert actual == 3

def test_min_count():

    actual = min_count(12)
    assert actual == 3

    actual = min_count(9)
    assert actual == 1

def test_bytelandian():

    test_cases = [
        {'input': 12, 'output': 13 },
        {'input': 8, 'output': 8 },
        {'input': 6, 'output': 6 },
        {'input': 25, 'output': 27 },
        {'input': 520, 'output': 689 },
        {'input': 1520, 'output': 2150 }
    ]

    # Naive Approach
    start = time.time()
    for test_case in test_cases:
        assert test_case['output'] == bytelandian_recurs(test_case['input'])
    end = time.time()
    print('Naive Approach', (end - start))

    # DP Memoization Approach
    start = time.time()
    for test_case in test_cases:
        assert test_case['output'] == bytelandian(test_case['input'])
    end = time.time()
    print('DP Memoization Approach', (end - start))

    # DP Iterative Approach
    start = time.time()
    for test_case in test_cases:
        assert test_case['output'] == bytelandian_dp(test_case['input'])
    end = time.time()
    print('DP Recursive Approach', (end - start))    

def test_max_loot():

    test_cases = [
        { 'input': [], 'output': 0},
        { 'input': [2, 3, 1000, 2000], 'output': 2003},
        { 'input': [5, 5, 10, 100, 10, 5], 'output': 110}
    ]

    # Naive Approach
    start = time.time()
    for test_case in test_cases:
        actual = max_loot_recurs(test_case['input'], 0)
        assert actual == test_case['output']
    end = time.time()
    print('Naive Approach', (end - start))
    
    # DP Memoization Approach
    start = time.time()
    for test_case in test_cases:
        ip = test_case['input']
        arr = [-1 for i in ip]
        assert test_case['output'] == max_loot_dp_mem(ip, 0, arr)
        print('arr------>', arr)
    end = time.time()
    print('DP Memoization Approach', (end - start))

    # DP Iteration Approach
    start = time.time()
    for test_case in test_cases:
        ip = test_case['input']
        actual = max_loot_dp_iter(ip, len(ip))
        print('actual----->', actual)
        # assert test_case['output'] == actual
    end = time.time()
    print('DP Iteration Approach', (end - start))