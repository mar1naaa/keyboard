import unittest
from functions import count_finger_load_vyzov

class Count_Finger_Load_Vyzov_TestCase(unittest.TestCase):
    def test_count_finger_load_vyzov(self):
        result =  count_finger_load_vyzov('text_1.txt')
        self.assertEqual(result, [1, 0, 0, 0, 1, 2, 0, 0, 0, 2])
if __name__ == '__main__':
    unittest.main()