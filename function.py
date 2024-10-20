import matplotlib.pyplot as plt
import numpy as np
from dict_finger import keyboard_finger_qwerty, vyzov_finger_count, keyboard_finger_vyzov, qwerty_finger_count

def read_file_and_remove_whitespace(filename):#Построчное считывание файла

  with open(filename, "r") as f:
    lines = f.readlines()
  return lines

def find_finger(character, keyboard_finger_qwerty):#Определение пальца по симвалу в qwerty
    character = character.lower()
    for finger_name, characters in keyboard_finger_qwerty.items():
        if character in characters:
            return finger_name
    return "Invalid character: {}".format(character)

def find_finger_2(character, keyboard_finger_vyzov):#Определение пальца по симвалу в vyzov
    character = character.lower()
    for finger_name, characters in keyboard_finger_vyzov.items():
        if character in characters:
            return finger_name
    return "Invalid character: {}".format(character)

def add_count(result, qwerty_finger_count):#Добавляет единицу в счётчик пальцев а qwerty
    if result in qwerty_finger_count:
        qwerty_finger_count[result] =+ 1
    return qwerty_finger_count

def add_count(result, vyzov_finger_count):#Добавляет единицу в счётчик пальцев а vyzov
    if result in vyzov_finger_count:
        vyzov_finger_count[result] =+ 1
    return vyzov_finger_count

def plot_finger_usage(layout1, layout2):
    """
    Функция для построения горизонтальной гистограммы с количеством нажатий пальцами
    для двух раскладок клавиатуры.

    - layout1: список количества нажатий для йцукен
    - layout2: список количества нажатий для вызов

    """
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)',
           'Большой (правая)', 'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
          '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    # Позиции столбцов на оси Y
    index = np.arange(len(fingers))

    # Ширина столбцов
    bar_width = 0.35

    # Построение горизонтальной гистограммы
    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width/2, layout1[i], bar_width, label='Йцукен' if i == 0 else "", color=colors[i], alpha=0.7)
        plt.barh(index[i] + bar_width/2, layout2[i], bar_width, label='Вызов' if i == 0 else "", color=colors[i], alpha=1.0)

    # Добавление подписей и заголовков
    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.title('Сравнение нагрузок на пальцы в раскладках йцукен и вызов')
    plt.yticks(index, fingers)

    # Легенда
    plt.legend()

    # Показ гистограммы
    plt.tight_layout()
    plt.show()