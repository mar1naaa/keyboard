"""
Данный скрипт анализирует текстовый файл, подсчитывает нагрузку на пальцы
при наборе текста в двух клавиатурных раскладках: ЙЦУКЕН и ВЫЗОВ.
Также вычисляет процент нагрузки на левую и правую руки для каждой раскладки
и выводит результаты, включая визуализацию в виде гистограммы.
Используемые функции:
 count_finger_load_qwerty(text): Подсчитывает нагрузку на пальцы (ЙЦУКЕН).
- count_finger_load_vyzov(text): Подсчитывает нагрузку на пальцы (ВЫЗОВ).
- load_hand_left(list): Вычисляет процент нагрузки на левую руку.
- load_hand_right(list): Вычисляет процент нагрузки на правую руку.
- vyvod_gistogramma(layout1, layout2): Вывод итоговой гистограммы.
Входные данные:
- text (str): Путь к текстовому файлу, вводится пользователем.
Выводимые данные:
Нагрузка на левую и правую руки в процентах для раскладок: ЙЦУКЕН и Вызов.
- Гистограмма, показывающая нагрузку на каждый палец в обеих раскладах.
Пример использования:
Введите файл с текстом: ваш_файл_с_текстом.txt
ЙЦУКЕН
Нагрузка на левую руку в процентах: X% Нагрузка на правую руку в процентах: Y%
ЫЗОВ
Нагрузка на левую руку в процентах: Z% Нагрузка на правую руку в процентах: W%
"""

from function import get_hand_and_finger, get_hand_and_finger_1, \
    count_digrams_with_layout, vyvod_gistogramma3
from dict_finger import keyboard_finger_dictor, \
    keyboard_finger_qwerty, keyboard_finger_scoropis, keyboard_finger_vyzov
if __name__ == "__main__":

    input_file = 'digrams.txt'
    left_qwerty, right_qwerty = count_digrams_with_layout(
        input_file, keyboard_finger_qwerty)
    left_vyzov, right_vyzov = count_digrams_with_layout(
        input_file, keyboard_finger_vyzov)
    left_dictor, right_dictor = count_digrams_with_layout(
        input_file, keyboard_finger_dictor)
    left_scoropis, right_scoropis = count_digrams_with_layout(
        input_file, keyboard_finger_scoropis)
    lv = [left_qwerty, left_vyzov, left_dictor, left_scoropis]
    rv = [right_qwerty, right_vyzov, right_dictor, right_scoropis]
    vyvod_gistogramma3(lv, rv)
    print("ЙЦУКЕН:")
    print(f"Диграммы, нажатые левой рукой: {left_qwerty}")
    print(f"Диграммы, нажатые правой рукой: {right_qwerty}")

    print("\nВЫЗОВ:")
    print(f"Диграммы, нажатые левой рукой: {left_vyzov}")
    print(f"Диграммы, нажатые правой рукой: {right_vyzov}")

    print("\nДИКТОР:")
    print(f"Диграммы, нажатые левой рукой: {left_dictor}")
    print(f"Диграммы, нажатые правой рукой: {right_dictor}")

    print("\nСКОРОПИСЬ:")
    print(f"Диграммы, нажатые левой рукой: {left_scoropis}")
    print(f"Диграммы, нажатые правой рукой: {right_scoropis}")
