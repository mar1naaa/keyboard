"""
Лабораторная работа №4
Считает количество диграмм,
нажатых "удобным" перебором
в 4 раскладках
"Удобный" перебор: на левой руке - слева направо,
на правой руке - справа налево,
то есть от мизинца до большого пальца
"""

from function import count_digrams_with_layout, vyvod_gistogramma3
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
