"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""
import dict_finger
import matplotlib.pyplot as plt
import numpy as np


def get_hand_and_finger(char, fingers_dict):
    """Определяет руку, которым нажимается символ"""
    for finger, keys in fingers_dict.items():
        if char.lower() in keys:
            return finger.split("f")[0]
    return None


def get_hand_and_finger_1(char, fingers_dict):
    """Определяет палец,
    которым нажимается символ"""
    for finger, keys in fingers_dict.items():
        if char.lower() in keys:
            return finger.split("f")[1]
    return None


def count_digrams_with_layout_1(filename, fingers_dict):
    """Считает количество диграмм для выбранной раскладки"""
    left_count_digrams = 0
    right_count_digrams = 0
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
                    left_count_digrams += 1
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4') or \
                        (first_hand_1 == "i5" and second_hand_1 == 'i3')\
                            or (first_hand_1 == "i5" and
                                second_hand_1 == 'i2') or \
                            (first_hand_1 == "i5" and
                                second_hand_1 == 'i1'):
                        left_hand_digrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3') or \
                        (first_hand_1 == "i4" and second_hand_1 == 'i2')\
                            or (first_hand_1 == "i4" and
                                second_hand_1 == 'i1'):
                        left_hand_digrams += 1
                    elif (first_hand_1 == "i3" and second_hand_1 == 'i2') or \
                        (first_hand_1 == "fi3" and
                         second_hand_1 == 'i1'):
                        left_hand_digrams += 1
                    elif first_hand_1 == "i2" and second_hand_1 == 'i1':
                        left_hand_digrams += 1
                elif first_hand == "r" and second_hand == "r":
                    right_count_digrams += 1
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4') or (
                            first_hand_1 == "i5" and second_hand_1 == 'i3') \
                            or (first_hand_1 == "i5" and
                                second_hand_1 == 'i2') or \
                            (first_hand_1 == "i5" and
                                second_hand_1 == 'i1'):
                        right_hand_digrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3') or \
                        (first_hand_1 == "i4" and second_hand_1 == 'i2')\
                            or (first_hand_1 == "i4" and
                                second_hand_1 == 'i1'):
                        right_hand_digrams += 1
                    elif (first_hand_1 == "i3" and second_hand_1 == 'i2') or \
                            (first_hand_1 == "i3" and second_hand_1 == 'i1'):
                        right_hand_digrams += 1
                    elif first_hand_1 == "i2" and second_hand_1 == 'i1':
                        right_hand_digrams += 1
    return left_count_digrams, right_count_digrams, \
        left_hand_digrams, right_hand_digrams


def count_trigrams_with_layout(filename, fingers_dict):
    """Считает количество триграмм для выбранной раскладки"""
    left_count_trigrams = 0
    right_count_trigrams = 0
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
                if first_hand == "l" and second_hand == "l" \
                        and third_hand == 'l':
                    left_count_trigrams += 1
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4'
                        and third_hand_1 == 'i3') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4'
                            and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4'
                            and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3'
                            and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3'
                            and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i2'
                            and third_hand_1 == 'i1'):
                        left_hand_trigrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3'
                          and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i4" and second_hand_1 == 'i3'
                            and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i4" and second_hand_1 == 'i2'
                            and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i3" and second_hand_1 == 'i2'
                            and third_hand_1 == 'i1'):
                        left_hand_trigrams += 1
                if first_hand == "r" and second_hand == "r" \
                        and third_hand == 'r':
                    right_count_trigrams += 1
                    if (first_hand_1 == "i5" and second_hand_1 == 'i4'
                        and third_hand_1 == 'i3') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4'
                            and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i4'
                            and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3'
                            and third_hand_1 == 'i2') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i3'
                            and third_hand_1 == 'i1') \
                        or (first_hand_1 == "i5" and second_hand_1 == 'i2'
                            and third_hand_1 == 'i1'):
                        right_hand_trigrams += 1
                    elif (first_hand_1 == "i4" and second_hand_1 == 'i3'
                          and third_hand_1 == 'i2')\
                        or (first_hand_1 == "i4" and second_hand_1 == 'i3'
                            and third_hand_1 == 'i1')\
                        or (first_hand_1 == "i4" and second_hand_1 == 'i2'
                            and third_hand_1 == 'i1')\
                        or (first_hand_1 == "i3" and second_hand_1 == 'i2'
                            and third_hand_1 == 'i1'):
                        right_hand_trigrams += 1
    return left_count_trigrams, right_count_trigrams, \
        left_hand_trigrams, right_hand_trigrams


def split_into_digrams(word):
    """Разделяет слово на диграммы"""
    digrams = []
    for i in range(len(word) - 1):
        digrams.append(word[i:i + 2])
    return digrams


def split_into_trigrams(word):
    """Разделяет слово на триграммы"""
    trigrams = []
    for i in range(len(word) - 2):
        trigrams.append(word[i:i + 3])
    return trigrams


def vyvod_gistogramma4(layout7, layout8):
    plt.figure(figsize=(15, 6))
    rasklads = ['Количество диграмм для левой руки',
                'Удобные диграммы для левой руки',
                'Количество диграмм для правой руки',
                'Удобные диграммы для правой руки',
                'Количество триграмм для левой руки',
                'Удобные триграммы для левой руки',
                'Количество триграмм для правой руки',
                'Удобные триграммы для правой руки']
    color = 'red'
    color_1 = 'blue'

    index = np.arange(len(rasklads))
    bar_width = 0.2

    for i in range(len(rasklads)):
        plt.barh(index[i] - bar_width / 2, layout7[i], bar_width,
                 label='Йцукен' if i == 0 else "", color=color,
                 alpha=0.7)
        plt.barh(index[i] + bar_width / 2, layout8[i], bar_width,
                 label='Вызов' if i == 0 else "", color=color_1,
                 alpha=1.0)

    plt.yticks(index, rasklads)
    plt.xlabel(' Количество диграмм и триграмм')
    plt.title('Диграммы и триграммы, нажатые удобным '
              'перебором в раскладках ЙЦУКЕН'
              ' и ВЫЗОВ, файл 1grams-3.txt')
    plt.legend()
    plt.tight_layout()
    plt.show()
