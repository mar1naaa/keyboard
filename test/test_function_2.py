import unittest

from dict_finger import keyboard_finger_qwerty
from function_2 import find_finger, character

class FindFingerTestCase(unittest.TestCase):
    def test_fun_2(self):
        result = find_finger(character, keyboard_finger_qwerty)
        self.assertEqual(result, 'lfi2')

if __name__== 'function_2.py':
    unittest.main()
