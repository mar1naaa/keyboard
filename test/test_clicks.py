import pytest # type: ignore
from function import clicks 

@pytest.fixture
def layout_data():
    """
    Фикстура для макетов с количеством нажатий
    """
    layout_1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    layout_2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    layout_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    layout_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return layout_1, layout_2, layout_3, layout_4

@pytest.fixture
def expected_keys():
    return [
        'левый мизинец', 'левый безымянный', 'левый средний',
        'левый указательный', 'левый большой',
        'правый большой', 'правый указательный', 'правый средний',
        'правый безымянный', 'правый мизинец'
    ]

def test_clicks_structure(layout_data, expected_keys):
    """
    Проверяет структуру и корректность ключей в результатах
    """
    layout_1, layout_2, layout_3, layout_4 = layout_data
    results = clicks(layout_1, layout_2, layout_3, layout_4)
    
    assert len(results) == 4 
    
    for result in results:
        assert isinstance(result, dict) 
        assert set(result.keys()) == set(expected_keys) 

def test_clicks_values(layout_data):
    """
    Проверяет корректность значений в словарях
    """
    layout_1, layout_2, layout_3, layout_4 = layout_data
    results = clicks(layout_1, layout_2, layout_3, layout_4)
    
    for i, layout in enumerate(layout_data):
        result = results[i]
        assert list(result.values()) == layout 
