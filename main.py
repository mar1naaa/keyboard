"""
Данный скрипт анализирует текстовый файл, подсчитывает нагрузку на пальцы
при наборе текста в двух клавиатурных раскладках: ЙЦУКЕН и ВЫЗОВ.
Также вычисляет процент нагрузки на левую и правую руки для каждой раскладки
и выводит результаты, включая визуализацию в виде гистограммы.

Используемые функции:
- count_finger_load_qwerty(text): Подсчитывает нагрузку на пальцы (ЙЦУКЕН).
- count_finger_load_vyzov(text): Подсчитывает нагрузку на пальцы (ВЫЗОВ).
- load_hand_left(list): Вычисляет процент нагрузки на левую руку.
- load_hand_right(list): Вычисляет процент нагрузки на правую руку.
- vyvod_gistogramma(layout1, layout2): Вывод итоговой гистограммы.

Входные данные:
- text (str): Путь к текстовому файлу, вводится пользователем.

Выводимые данные:
- Нагрузка на левую и правую руки в процентах для раскладок: ЙЦУКЕН и Вызов.
- Гистограмма, показывающая нагрузку на каждый палец в обеих раскладах.

Пример использования:
Введите файл с текстом: ваш_файл_с_текстом.txt
ЙЦУКЕН
Нагрузка на левую руку в процентах: X% Нагрузка на правую руку в процентах: Y%
ВЫЗОВ
Нагрузка на левую руку в процентах: Z% Нагрузка на правую руку в процентах: W%
"""

from function import *

if __name__ == "__main__":

    text = "/Users/marinazhinzhikova/Documents/keyboard/1grams-3.txt"
    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)

    left_qwerty = load_hand_left(qwerty_finger_load)
    right_qwerty = load_hand_right(qwerty_finger_load)
    left_vyzov = load_hand_left(vyzov_finger_load)
    right_vyzov = load_hand_right(vyzov_finger_load)
    print('ЙЦУКЕН')
    print('Нагрузка на левую руку в процентах:', left_qwerty, '%')
    print('Нагрузка на правую руку в процентах:', right_qwerty, '%')
    print('ВЫЗОВ')
    print('Нагрузка на левую руку в процентах:', left_vyzov, '%')
    print('Нагрузка на правую руку в процентах:', right_vyzov, '%')
    vyvod_gistogramma(qwerty_finger_load, vyzov_finger_load)
