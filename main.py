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
    input_file = "digrams.txt"
    left_count_qwerty, right_count_qwerty, \
        left_qwerty, right_qwerty = \
        count_digrams_with_layout(input_file, keyboard_finger_qwerty)
    left_count_vyzov, right_count_vyzov, \
        left_vyzov, right_vyzov = \
        count_digrams_with_layout(input_file, keyboard_finger_vyzov)
    left_count_dictor, right_count_dictor, \
        left_dictor, right_dictor = \
        count_digrams_with_layout(input_file, keyboard_finger_dictor)
    left_count_scoropis, right_count_scoropis, \
        left_scoropis, right_scoropis = \
        count_digrams_with_layout(input_file, keyboard_finger_scoropis)
    lv = [left_qwerty,
          left_vyzov,
          left_dictor,
          left_scoropis]
    lv_1 = [left_count_qwerty, left_count_vyzov,
            left_count_dictor, left_count_scoropis]
    rv = [right_qwerty,
          right_vyzov,
          right_dictor,
          right_scoropis]
    rv_1 = [right_count_qwerty, right_count_vyzov,
            right_count_dictor, right_count_scoropis]
    print("ЙЦУКЕН:")
    print(f"Диграммы, нажатые левой рукой: {left_count_qwerty}")
    print(f"Удобные диграммы, нажатые левой рукой: {left_qwerty}")
    print(f"Диграммы, нажатые правой рукой: {right_count_qwerty}")
    print(f"Удобные диграммы, нажатые правой рукой: {right_qwerty}")

    print("\nВЫЗОВ:")
    print(f"Диграммы, нажатые левой рукой: {left_count_vyzov}")
    print(f"Удобные диграммы, нажатые левой рукой: {left_vyzov}")
    print(f"Диграммы, нажатые правой рукой: {right_count_vyzov}")
    print(f"Удобные диграммы, нажатые правой рукой: {right_vyzov}")

    print("\nДИКТОР:")
    print(f"Диграммы, нажатые левой рукой: {left_count_dictor}")
    print(f"Удобные диграммы, нажатые левой рукой: {left_dictor}")
    print(f"Диграммы, нажатые правой рукой: {right_count_dictor}")
    print(f"Удобные диграммы, нажатые правой рукой: {right_dictor}")

    print("\nСКОРОПИСЬ:")
    print(f"Диграммы, нажатые левой рукой: {left_count_scoropis}")
    print(f"Удобные диграммы, нажатые левой рукой: {left_scoropis}")
    print(f"Диграммы, нажатые правой рукой: {right_count_scoropis}")
    print(f"Удобные диграммы, нажатые правой рукой: {right_scoropis}")
    vyvod_gistogramma3(lv, rv, lv_1, rv_1)
