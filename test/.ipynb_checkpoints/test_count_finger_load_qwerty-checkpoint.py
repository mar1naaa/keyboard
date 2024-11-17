import unittest
from functions import count_finger_load_qwerty

class Count_Finger_Load_QwertyTestCase(unittest.TestCase):
    def test_count_finger_load_qwerty(self):
        result =  count_finger_load_qwerty('text_1.txt')
        self.assertEqual(result, [1, 2, 0, 0, 1, 0, 0, 0, 0])
if __name__ == '__main__':
    unittest.main()