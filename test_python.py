import math
"""
    Файл содержит тесты для функций общего пользования
"""

"""
    Тесты для функции map
"""
def test_map_lambda():
    l_input = [1, 1, 1, 1, 1]
    l_result = [2, 2, 2, 2, 2]
    assert list(map(lambda x: x + 1, l_input)) == l_result

def test_map_char():
    l_input = ["1", "1", "1", "1", "1"]
    l_result = [1, 1, 1, 1, 1]
    assert (list(map(int, l_input))) == l_result


"""
    Тесты для filter
"""
def test_filter_plain():
    l_input = [1,2,3,4,5,6,7]
    l_result = [4,5,6,7]
    assert list(filter(lambda x: x > 3, l_input)) == l_result

def test_filter_even():
    l_input = [1,2,3,4,5,6,7]
    l_result = [2,4,6]
    assert list(filter(lambda x: x % 2 == 0, l_input)) == l_result

    
"""
    Тесты для функции sorted
"""
def test_sorted_plain():
    l_input = [7,2,6,4,5,3,1]
    l_result = [1,2,3,4,5,6,7]
    assert sorted(l_input) == l_result

def test_sorted_reverse():
    l_input = [7,2,6,4,5,3,1]
    l_result = [7,6,5,4,3,2,1]
    assert sorted(l_input,reverse=True) == l_result


"""
    Тест Pi
"""
def test_Pi():
    assert math.pi == 3.141592653589793


"""
    Тест sqrt
"""
def test_sqrt_plain():
    assert math.sqrt(4.0) == 2.0

def test_sqrt_negative():
    try:
       math.sqrt(-4.0)
    except Exception as ex:
        assert isinstance(ex,ValueError)


"""
    Тест pow
"""
def test_pow_plain():
    assert pow(2,1) == 2
    assert pow(2,2) == 4
    assert pow(4, 0.5) == 2

def test_pow_negative():
    assert pow(-4, 0.5) == 1.2246467991473532e-16+2j

"""
    Тест hypot
"""
def test_hypot_plain():
    x = 2
    y = 4
    assert math.hypot(x,y) == math.sqrt(x*x + y*y)
    x = -2
    y = 0
    assert math.hypot(x,y) == math.sqrt(x*x + y*y)
    x = -8
    y = -5
    assert math.hypot(x,y) == math.sqrt(x*x + y*y)