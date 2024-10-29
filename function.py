"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""
import dict_finger
import matplotlib.pyplot as plt
import numpy as np
from dict_finger import *


def find_finger(character, keyboard_layout):
    """
        Определяет, какой палец используется
        для набора данного символа на клавиатуре.
    """
    flag = 0
    for finger_name, characters in keyboard_layout.items():
        if character in characters:
            return finger_name, flag
        else:
            if keyboard_layout == keyboard_finger_vyzov:
                for finger_name, characters \
                      in keyboard_finger_vyzov_dop.items():
                    if character in characters:
                        flag = 1
                        return finger_name, flag
            else:
                if keyboard_layout == keyboard_finger_qwerty:
                    for finger_name, characters \
                            in keyboard_finger_qwerty_dop.items():
                        if character in characters:
                            flag = 1
                            return finger_name, flag
    else:
        return "Invalid character: {}".format(character), flag


def count_finger_load_qwerty(text):
    """
        Подсчитывает нагрузку на пальцы, использованные при наборе текста
        на клавиатурной раскладке QWERTY.
    """
    for character in text:
        finger_name, flag_nado = \
             find_finger(character.lower(), keyboard_finger_qwerty)
        if finger_name in dict_finger.qwerty_finger_count:
            dict_finger.qwerty_finger_count[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5'
                dict_finger.qwerty_finger_count[shift_finger] += 1
    layout_1 = list(qwerty_finger_count.values())
    return layout_1


def count_finger_load_vyzov(text):
    """
        Подсчитывает нагрузку на пальцы, использованные при наборе текста
        в раскладке "Вызов".
    """
    for character in text:
        finger_name, flag_nado = \
             find_finger(character.lower(), keyboard_finger_vyzov)
        if finger_name in dict_finger.vyzov_finger_count:
            dict_finger.vyzov_finger_count[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5'
                dict_finger.vyzov_finger_count[shift_finger] += 1
    layout_2 = list(vyzov_finger_count.values())
    return layout_2


def vyvod_gistogramma(layout1, layout2):
    """
        Строит горизонтальную гистограмму для сравнения нагрузки на пальцы
        при использовании двух различных клавиатурных раскладок.
    """
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)',
               'Указательный (левая)', 'Большой (левая)',
               'Указательный (правая)', 'Средний (правая)',
               'Безымянный (правая)', 'Мизинец (правая)']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99',
              '#c2c2f0', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    index = np.arange(len(fingers))
    bar_width = 0.35
    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width / 2, layout1[i], bar_width,
                 label='Йцукен' if i == 0 else "", color=colors[i], alpha=0.7)
        plt.barh(index[i] + bar_width / 2, layout2[i], bar_width,
                 label='Вызов' if i == 0 else "", color=colors[i], alpha=1.0)
    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.title('Сравнение нагрузок на пальцы в раскладках йцукен и вызов')
    plt.yticks(index, fingers)
    plt.legend()
    plt.tight_layout()
    plt.show()


def load_hand_left(list):
    """
      Вычисляет процент нагрузки
      на левую руку на основе значений из переданного списка.
    """
    start_index = 0
    end_index = 5
    start_index_1 = 0
    end_index_1 = 9
    partial_sum = sum(list[start_index:end_index])
    general_sum = sum(list[start_index_1:end_index_1])
    procent = int((partial_sum * 100)/general_sum)
    return procent


def load_hand_right(list):
    """
    Вычисляет процент нагрузки
    на правую руку на основе значений из переданного списка.
    """
    start_index = 5
    end_index = 9
    start_index_1 = 0
    end_index_1 = 9
    partial_sum = sum(list[start_index:end_index])
    general_sum = sum(list[start_index_1:end_index_1])
    procent = int((partial_sum * 100) / general_sum)
    return procent
