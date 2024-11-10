"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""

import matplotlib.pyplot as plt
import numpy as np
from dict_finger import *

def find_finger(character, keyboard_layout):
  """
     Определяет, какой палец используется для набора данного символа на клавиатуре.

     Функция принимает символ и раскладку клавиатуры, а затем проверяет,
     каким пальцем обычно набирается этот символ согласно заданной раскладке.

     Параметры:
     - character (str): Символ, для которого нужно определить палец.
     - keyboard_layout (dict): Словарь, в котором ключами являются имена пальцев,
                               а значениями - строки символов, которые они могут набирать.

     Возвращает:
     - str: Название пальца, который используется для набора символа.
     - str: Сообщение об ошибке, если символ не найден в раскладке.

     Пример использования:
     >>> layout = {
     ...     'Index Finger': 'd f g h j k l',
     ...     'Middle Finger': 'e r t',
     ...     'Ring Finger': 'w s x',
     ...     'Little Finger': 'q a z',
     ...     'Thumb': 'space'
     ... }
     >>> find_finger('g', layout)
     'Index Finger'

     >>> find_finger('x', layout)
     'Ring Finger'

     >>> find_finger('z', layout)
     'Little Finger'

     >>> find_finger('!', layout)
     'Invalid character: !'
     """
  character = character.lower()
  for finger_name, characters in keyboard_layout.items():
    if character in characters:
        return finger_name
  return "Invalid character: {}".format(character)

def count_finger_load_qwerty(text):
  """
     Подсчитывает нагрузку на пальцы, использованные при наборе текста
     на клавиатурной раскладке QWERTY.

     Функция открывает файл по указанному пути, считывает его содержимое
     и определяет, сколько раз каждый палец использовался для набора символов
     в тексте. Результаты подсчета возвращаются в виде списка,
     который отражает количество нажатий каждым пальцем.

     Параметры:
     - text (str): Путь к файлу, содержащему текст для анализа.

     Возвращает:
     - list: Список, в котором содержатся количества нажатий для каждого пальца
              в порядке их использования.

     Пример использования:
     >>> finger_load = count_finger_load_qwerty('path_to_your_file.txt')
     >>> print(finger_load)  # Выводит список с количеством нажатий для каждого пальца.
     """
  with open(text, "r", encoding='utf-8') as f:
    text = f.read()
  for character in text:
    finger_name = find_finger(character, keyboard_finger_qwerty)
    if finger_name in dict_finger.qwerty_finger_count:
      dict_finger.qwerty_finger_count[finger_name] += 1
  layout_1 = list(qwerty_finger_count.values())
  return layout_1

def count_finger_load_vyzov(text):
  """
      Подсчитывает нагрузку на пальцы, использованные при наборе текста
      в раскладке "Вызов".

      Функция открывает файл по указанному пути, считывает его содержимое
      и определяет, сколько раз каждый палец использовался для набора символов
      в тексте. Результаты подсчета возвращаются в виде списка,
      который отражает количество нажатий каждым пальцем.

      Параметры:
      - text (str): Путь к файлу, содержащему текст для анализа.

      Возвращает:
      - list: Список, в котором содержатся количества нажатий для каждого пальца
               в порядке их использования.

      Пример использования:
      >>> finger_load = count_finger_load_vyzov('path_to_your_file.txt')
      >>> print(finger_load)  # Выводит список с количеством нажатий для каждого пальца.
      """
  with open(text, "r", encoding='utf-8') as f:
    text = f.read()
  for character in text:
    finger_name = find_finger(character, keyboard_finger_vyzov)
    if finger_name in dict_finger.vyzov_finger_count:
      vyzov_finger_count[finger_name] += 1
  layout_2 = list(vyzov_finger_count.values())
  return layout_2

def vyvod_gistogramma(layout1, layout2):
  """
      Строит горизонтальную гистограмму для сравнения нагрузки на пальцы
      при использовании двух различных клавиатурных раскладок.

      Функция принимает два списка, содержащие количества нажатий для
      каждого пальца при наборе текста в двух раскладках, и отображает
      горизонтальную гистограмму с различными цветами для каждой раскладки.

      Параметры:
      - layout1 (list): Список, содержащий количества нажатий для пальцев
                        в первой раскладке (например, QWERTY).
      - layout2 (list): Список, содержащий количества нажатий для пальцев
                        во второй раскладке (например, Вызов).

      Возвращает:
      - None: Функция выводит гистограмму на экран.

      Пример использования:
      >>> layout1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
      >>> layout2 = [15, 25, 35, 45, 55, 65, 75, 85, 95]
      >>> vyvod_gistogramma(layout1, layout2)  # Выводит гистограмму для двух раскладок.
      """
  fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)',
               'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
  colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
  index = np.arange(len(fingers))
  bar_width = 0.35
  for i in range(len(fingers)):
    plt.barh(index[i] - bar_width / 2, layout1[i], bar_width, label='Йцукен' if i == 0 else "", color=colors[i],
               alpha=0.7)
    plt.barh(index[i] + bar_width / 2, layout2[i], bar_width, label='Вызов' if i == 0 else "", color=colors[i],
               alpha=1.0)
  plt.ylabel('Пальцы')
  plt.xlabel('Количество нажатий')
  plt.show()

def load_hand_left(list):
  """
      Вычисляет процент нагрузки на левую руку на основе значений из переданного списка.

      Функция принимает список, который содержит нагрузки (например, количество нажатий пальцев),
      и вычисляет процент нагрузки для первых 5 значений по сравнению с общим значением
      для первых 10 элементов списка.

      Параметры:
      - list (list): Список чисел, представляющий нагрузки, из которых нужно вычислить проценты.

      Возвращает:
      - int: Процент нагрузки на левую руку, вычисляемый как отношение суммы первых 5 значений
              к общей сумме первых 10 значений, умноженное на 100.

      Пример использования:
      >>> loads = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
      >>> percentage = load_hand_left(loads)
      >>> print(percentage)  # Выводит процент нагрузки на левую руку.
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
      Вычисляет процент нагрузки на правую руку на основе значений из переданного списка.

      Функция принимает список, который содержит нагрузки (например, количество нажатий пальцев),
      и вычисляет процент нагрузки для значений с 5-го по 8-е по сравнению с общим значением
      для первых 10 элементов списка.

      Параметры:
      - list (list): Список чисел, представляющий нагрузки, из которых нужно вычислить проценты.

      Возвращает:
      - int: Процент нагрузки на правую руку, вычисляемый как отношение суммы значений с 5-го по 8-е
              к общей сумме первых 10 значений, умноженное на 100.

      Пример использования:
      >>> loads = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
      >>> percentage = load_hand_right(loads)
      >>> print(percentage)  # Выводит процент нагрузки на правую руку.
      """
  start_index = 5
  end_index = 9
  start_index_1 = 0
  end_index_1 = 9
  partial_sum = sum(list[start_index:end_index])
  general_sum = sum(list[start_index_1:end_index_1])
  procent = int((partial_sum * 100) / general_sum)
  return procent
def clicks:
  fing=['левый мизинец','левый безымянный','левый средний','левый указательный','левый большой','правый большой',
  'правый указательный','правый средний','правый безымянный','правый мизинец']
  fing_d_qwerty= dict(zip(fing,layout_1))
  fing_d_vyzov=dict(zip(fing,layout_2))
  return fing_d_qwerty,fing_d_vyzov
