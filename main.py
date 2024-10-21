"""
основной? модуль

"""

from function import *

if __name__ == "__main__":
    
    filename = "/Users/marinazhinzhikova/Documents/keyboard/readtext.txt"
    text = read_file(filename)
    text = ''.join(text)
    finger = find_finger_qwerty(text, keyboard_finger_qwerty)
    finger_count = count_finger_qwerty(finger, qwerty_finger_count)
    
