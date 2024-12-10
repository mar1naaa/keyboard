import pytest
from function import load_hand_left

@pytest.fixture
def sample_data():
    return [10, 20, 30, 40, 50, 60, 70, 80, 90]

@pytest.fixture
def invalid_data_zero_sum():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_load_hand_left_valid_data(sample_data):
    result = load_hand_left(sample_data)
    assert result == 33

def test_load_hand_left_zero_sum(invalid_data_zero_sum):
    with pytest.raises(ZeroDivisionError):
        load_hand_left(invalid_data_zero_sum)
