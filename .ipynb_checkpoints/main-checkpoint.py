from function import *

if __name__ == "__main__":

    text = input("Enter the path to the text file: ")
    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)
    print(qwerty_finger_load)
    print(vyzov_finger_load)