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
    
