"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""
import dict_finger
import matplotlib.pyplot as plt
import numpy as np


def get_hand_and_finger(char, fingers_dict):
    """Определяет руку и палец, которым нажимается символ"""
    for finger, keys in fingers_dict.items():
        if char.lower() in keys:
            return finger.split("f")[0]
    return None


def get_hand_and_finger_1(char, fingers_dict):
    """Определяет руку и палец, которым нажимается символ"""
    for finger, keys in fingers_dict.items():
        if char.lower() in keys:
            return finger.split("f")[1]
    return None


def count_digrams_with_layout(filename, fingers_dict):
    """Считает количество диграмм для выбранной раскладки"""
    left_hand_digrams = 0
    right_hand_digrams = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            digram = line.strip()
            if len(digram) == 2:
                first, second = digram[0], digram[1]
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


def vyvod_gistogramma3(layout7, layout8):
    """
        Вывод в виде графика для диграмм, нажатых удобным перебором
    """
    plt.figure(figsize=(10, 6))
    rasklads = ['ЙЦУКЕН', 'ВЫЗОВ', 'ДИКТОР', 'СКОРОПИСЬ']
    color1 = '#ff0033'
    color2 = '#0000ff'

    index = np.arange(len(rasklads))
    bar_width = 0.2

    for i in range(len(rasklads)):
        plt.barh(index[i] - bar_width / 2, layout7[i], bar_width, label='Левая рука' if i == 0 else "", color=color1,
                 alpha=0.7)
        plt.barh(index[i] + bar_width / 2, layout8[i], bar_width, label='Правая рука' if i == 0 else "", color=color2,
                 alpha=1.0)

    plt.yticks(index, rasklads)
    plt.xlabel('Количество диграмм')
    plt.ylabel('Раскладки')
    plt.title('Диграммы, нажатые удобным перебором,'
              'в  различных раскладках, файл digrams')
    plt.legend()
    plt.tight_layout()
    plt.show()
