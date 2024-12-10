import pytest
from function import find_finger

@pytest.fixture
def keyboard_layout_qwerty():
    from dict_finger import keyboard_finger_qwerty
    return keyboard_finger_qwerty

@pytest.fixture
def keyboard_layout_qwerty_dop():
    from dict_finger import keyboard_finger_qwerty_dop
    return keyboard_finger_qwerty_dop

def test_find_finger_valid_character_qwerty(keyboard_layout_qwerty):
    character = "a"
    result = find_finger(character, keyboard_layout_qwerty)
    assert isinstance(result, tuple), "Результат должен быть кортежем"
    assert result[0] is not None, "Имя пальца должно быть определено"
    assert result[1] == 0, "Флаг должен быть равен 0 для основного символа"

def test_find_finger_invalid_character(keyboard_layout_qwerty):
    character = "w"  # Символ не существует на клавиатуре
    result = find_finger(character, keyboard_layout_qwerty)
    assert isinstance(result, tuple), "Результат должен быть кортежем"
    assert "Invalid character" in result[0], "Сообщение об ошибке должно быть корректным"
    assert result[1] == 0, "Флаг должен быть равен 0 для недопустимого символа"

def test_find_finger_dop_layout(keyboard_layout_qwerty, keyboard_layout_qwerty_dop):
    from dict_finger import keyboard_finger_qwerty
    character = "!"
    result = find_finger(character, keyboard_finger_qwerty)
    assert isinstance(result, tuple), "Результат должен быть кортежем"
    assert result[0] is not None, "Имя пальца должно быть определено"
    assert result[1] == 1, "Флаг должен быть равен 1 для символов из доп. раскладки"
