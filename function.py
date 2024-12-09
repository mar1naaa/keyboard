"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""
import dict_finger
import matplotlib.pyplot as plt
import numpy as np
from dict_finger import keyboard_finger_qwerty, \
    keyboard_finger_dictor_dop, keyboard_finger_dictor, \
    keyboard_finger_qwerty_dop, keyboard_finger_scoropis, \
    keyboard_finger_scoropis_dop, keyboard_finger_vyzov, \
    keyboard_finger_vyzov_dop, vyzov_finger_count, \
    dictor_finger_count, qwerty_finger_count, \
    scoropis_finger_count, penalty_table_qwerty, \
    penalty_table_qwerty_dop, penalty_table_vyzov,\
    penalty_table_vyzov_dop, count_penalty_qwerty,\
    count_penalty_vyzov


def get_hand_and_finger(char, fingers_dict):
    """Определяет руку и палец, которым нажимается символ"""
    for finger, keys in fingers_dict.items():
        if char.lower() in keys:
            return finger.split("f")[0]
    return None


def get_hand_and_finger_1(char, fingers_dict):
    for finger, keys in fingers_dict.items():
        if char.lower() in keys:
            return finger.split("f")[1]
    return None


def count_digrams_with_layout_1(filename, fingers_dict):
    """Считает количество диграмм для выбранной раскладки"""
    left_hand_digrams = 0
    right_hand_digrams = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            digram = line.strip()
            digram = split_into_digrams(line)
            for symbol in digram:
                first, second = symbol[0], symbol[1]
                first_hand = get_hand_and_finger(first, fingers_dict)
                second_hand = get_hand_and_finger(second, fingers_dict)
                first_hand_1 = get_hand_and_finger_1(first, fingers_dict)
                second_hand_1 = get_hand_and_finger_1(second, fingers_dict)

                if first_hand == "l" and second_hand == "l":
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4') or (first_hand_1 == "i5" and second_hand_1 == 'i3')\
                            or (first_hand_1 == "i5" and second_hand_1 == 'i2') or (first_hand_1 == "i5" and second_hand_1 == 'i1'):
                        left_hand_digrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3') or (first_hand_1 == "i4" and second_hand_1 == 'i2')\
                            or (first_hand_1 == "i4" and second_hand_1 == 'i1'):
                        left_hand_digrams += 1
                    elif (first_hand_1 == "i3" and second_hand_1 == 'i2') or (first_hand_1 == "fi3" and second_hand_1 == 'i1'):
                        left_hand_digrams += 1
                    elif first_hand_1 == "i2" and second_hand_1 == 'i1':
                        left_hand_digrams += 1
                elif first_hand == "r" and second_hand == "r":
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4') or (
                            first_hand_1 == "i5" and second_hand_1 == 'i3') \
                            or (first_hand_1 == "i5" and second_hand_1 == 'i2') or (first_hand_1 == "i5" and second_hand_1 == 'i1'):
                        right_hand_digrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3') or (first_hand_1 == "i4" and second_hand_1 == 'i2')\
                            or (first_hand_1 == "i4" and second_hand_1 == 'i1'):
                        right_hand_digrams += 1
                    elif (first_hand_1 == "i3" and second_hand_1 == 'i2') or (first_hand_1 == "i3" and second_hand_1 == 'i1'):
                        right_hand_digrams += 1
                    elif first_hand_1 == "i2" and second_hand_1 == 'i1':
                        right_hand_digrams += 1
    return left_hand_digrams, right_hand_digrams


def count_trigrams_with_layout(filename, fingers_dict):
    """Считает количество триграмм для выбранной раскладки"""
    left_hand_trigrams = 0
    right_hand_trigrams = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            digram = line.strip()
            digram = split_into_trigrams(line)
            for symbol in digram:
                first, second, third = symbol[0], symbol[1], symbol[2]
                first_hand = get_hand_and_finger(first, fingers_dict)
                second_hand = get_hand_and_finger(second, fingers_dict)
                third_hand = get_hand_and_finger(third, fingers_dict)
                first_hand_1 = get_hand_and_finger_1(first, fingers_dict)
                second_hand_1 = get_hand_and_finger_1(second, fingers_dict)
                third_hand_1 = get_hand_and_finger_1(third, fingers_dict)
                if first_hand == "l" and second_hand == "l" and third_hand == 'l':
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4' and third_hand_1 == 'i3') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4' and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3' and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i2' and third_hand_1 == 'i1'):
                        left_hand_trigrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3' and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i4" and second_hand_1 == 'i3' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i4" and second_hand_1 == 'i2' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i3" and second_hand_1 == 'i2' and third_hand_1 == 'i1'):
                        left_hand_trigrams += 1
                if first_hand == "r" and second_hand == "r" and third_hand == 'r':
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4' and third_hand_1 == 'i3') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4' and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3' and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i2' and third_hand_1 == 'i1'):
                        right_hand_trigrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3' and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i4" and second_hand_1 == 'i3' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i4" and second_hand_1 == 'i2' and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i3" and second_hand_1 == 'i2' and third_hand_1 == 'i1'):
                        right_hand_trigrams += 1
    return left_hand_trigrams, right_hand_trigrams



def split_into_digrams(word):
    """Разделяет слово на диграммы"""
    digrams = []
    for i in range(len(word) - 1):
        digrams.append(word[i:i + 2])
    return digrams


def split_into_trigrams(word):
    """Разделяет слово на триграммы."""
    trigrams = []
    for i in range(len(word) - 2):
        trigrams.append(word[i:i + 3])
    return trigrams


def vyvod_gistogramma4(layout7, layout8):
    """Вывод в виде графика"""
    plt.figure(figsize=(10, 6))
    rasklads = ['Удобные диграммы для левой руки','Удобные диграммы для правой руки', 'Удобные триграммы для левой руки', 'Удобные триграммы для правой руки']
    color = 'red'
    color_1 = 'blue'

    index = np.arange(len(rasklads))
    bar_width = 0.2

    for i in range(len(rasklads)):
        plt.barh(index[i] - bar_width / 2, layout7[i], bar_width, label='ЙЦУКЕН' if i == 0 else "", color=color,
                 alpha=0.7)
        plt.barh(index[i] + bar_width / 2, layout8[i], bar_width, label='ВЫЗОМ' if i == 0 else "", color=color_1,
                 alpha=1.0)



    plt.yticks(index, rasklads)
    plt.xlabel(' Количество диграмм и триграмм')
    plt.title('Диграммы и триграммы, нажатые удобным перебором в раскладках ЙЦУКЕН' 
              'и ВЫЗОВ, файл 1grams-3.txt')
    plt.legend()
    plt.tight_layout()
    plt.show()

