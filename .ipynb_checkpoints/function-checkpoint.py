import matplotlib.pyplot as plt
import numpy as np
from dict_finger import *

def read_file(filename):#Построчное считывание файла

  with open(filename, "r") as f:
    text = [line.strip() for line in f.readlines()]
  return text
    
"""
def count_spaces(text): #кол-во пробелов в тексте
    qwerty_finger_count['lf1'] += text.count(' ')
    vyzov_finger_count['lf1'] += text.count(' ')
"""

def find_finger_qwerty(character, keyboard_finger_qwerty):#Определение пальца по символу в qwerty
    character = character.lower()
    for finger_name, characters in keyboard_finger_qwerty.items():
        if character in characters:
            return finger_name
    return "Invalid character: {}".format(character)

def find_finger_vyzov(character, keyboard_finger_vyzov):#Определение пальца по символу в vyzov
    character = character.lower()
    for finger_name, characters in keyboard_finger_vyzov.items():
        if character in characters:
            return finger_name
    return "Invalid character: {}".format(character)

def count_finger_qwerty(result, qwerty_finger_count):#Добавляет единицу в счётчик пальцев в qwerty
    if result in qwerty_finger_count:
        qwerty_finger_count[result] += 1
    return qwerty_finger_count

def ount_finger_vyzov(result, vyzov_finger_count):#Добавляет единицу в счётчик пальцев в vyzov
    if result in vyzov_finger_count:
        vyzov_finger_count[result] += 1
    return vyzov_finger_count

def vyvod_gistogramma(layout1, layout2):
    """
    Функция для построения горизонтальной гистограммы с количеством нажатий пальцами
    для двух раскладок клавиатуры.

    - layout1: список количества нажатий для йцукен
    - layout2: список количества нажатий для вызов

    """
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)', 'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    
    index = np.arange(len(fingers))
    bar_width = 0.35


    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width/2, layout1[i], bar_width, label='Йцукен' if i == 0 else "", color=colors[i], alpha=0.7)
        plt.barh(index[i] + bar_width/2, layout2[i], bar_width, label='Вызов' if i == 0 else "", color=colors[i], alpha=1.0)

    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.title('Сравнение нагрузок на пальцы в раскладках йцукен и вызов')
    plt.yticks(index, fingers)

    plt.legend()

    # Показ гистограммы
    plt.tight_layout()
    plt.show()