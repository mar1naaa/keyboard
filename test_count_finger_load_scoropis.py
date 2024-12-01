import pytest
from function import count_finger_load_scoropis

@pytest.fixture
def scoropis_layout():
    from dict_finger import keyboard_finger_scoropis, scoropis_finger_count
    return keyboard_finger_scoropis, scoropis_finger_count

@pytest.fixture
def test_text():
    return "А Жинжикова не дура!"

def test_count_finger_load_scoropis(scoropis_layout, test_text):
    keyboard_layout, finger_count = scoropis_layout
    
    result = count_finger_load_scoropis(test_text)
    
    assert isinstance(result, list), "Результат должен быть списком"
    assert len(result) == len(finger_count), "Размер результата должен соответствовать количеству пальцев"
    assert all(isinstance(value, int) for value in result), "Все значения нагрузки должны быть целыми числами"
    assert sum(result) > 0, "Нагрузка на пальцы не должна быть нулевой для текста"