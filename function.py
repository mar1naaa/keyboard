"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""

import matplotlib.pyplot as plt
import numpy as np
from dict_finger import *

def find_finger(character, keyboard_layout): #функция, определяющая какая буква/символ нажат
  character = character.lower()
  for finger_name, characters in keyboard_layout.items():
    if character in characters:
        return finger_name
  return "Invalid character: {}".format(character)

def count_finger_load_qwerty(text):#определяем какому пальцу принадлежит символ в йцукен
  with open(text, "r", encoding='utf-8') as f:
    text = f.read()
  for character in text:
    finger_name = find_finger(character, keyboard_finger_qwerty)
    if finger_name in dict_finger.qwerty_finger_count:
      dict_finger.qwerty_finger_count[finger_name] += 1
  return qwerty_finger_count

def count_finger_load_vyzov(text):#определяем какому пальцу принадлежит символ в вызов
  with open(text, "r", encoding='utf-8') as f:
    text = f.read()
  for character in text:
    finger_name = find_finger(character, keyboard_finger_vyzov)
    if finger_name in dict_finger.vyzov_finger_count:
      vyzov_finger_count[finger_name] += 1
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

    plt.tight_layout()
    plt.show()