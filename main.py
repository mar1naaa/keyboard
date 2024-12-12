"""
Лабораторная №5
Подсчитывает диграммы и триграммы
в раскладках ВЫЗОВ и ЙЦУКЕН
"""

from function import count_digrams_with_layout_1, \
    count_trigrams_with_layout, vyvod_gistogramma4
from dict_finger import keyboard_finger_qwerty, keyboard_finger_vyzov
if __name__ == "__main__":
    input_file = "1grams-3.txt"
    left_count_qwerty, right_count_qwerty, \
        left_qwerty, right_qwerty = \
        count_digrams_with_layout_1(input_file, keyboard_finger_qwerty)
    left_count_vyzov, right_count_vyzov, \
        left_vyzov, right_vyzov = \
        count_digrams_with_layout_1(input_file, keyboard_finger_vyzov)
    left_count_qwerty_tri, right_count_qwerty_tri, \
        left_qwerty_tri, right_qwerty_tri = \
        count_trigrams_with_layout(input_file, keyboard_finger_qwerty)
    left_count_vyzov_tri, right_count_vyzov_tri, \
        left_vyzov_tri, right_vyzov_tri = \
        count_trigrams_with_layout(input_file, keyboard_finger_vyzov)
    print("ЙЦУКЕН:")
    print(f"Диграммы, нажатые левой рукой: {left_count_qwerty}")
    print(f"Удобные диграммы, нажатые левой рукой: {left_qwerty}")
    print(f"Диграммы, нажатые правой рукой: {right_count_qwerty}")
    print(f"Удобные диграммы, нажатые правой рукой: {right_qwerty}")
    print(f"Триграммы, нажатые левой рукой: {left_count_qwerty_tri}")
    print(f"Удобные триграммы, нажатые левой рукой: {left_qwerty_tri}")
    print(f"Триграммы, нажатые правой рукой: {right_count_qwerty_tri}")
    print(f"Удобные триграммы, нажатые левой рукой: {right_qwerty_tri}")
    print("\nВЫЗОВ:")
    print(f"Диграммы, нажатые левой рукой: {left_count_vyzov}")
    print(f"Удобные диграммы, нажатые левой рукой: {left_vyzov}")
    print(f"Диграммы, нажатые правой рукой: {right_count_vyzov}")
    print(f"Удобные диграммы, нажатые правой рукой: {right_vyzov}")
    print(f"Триграммы, нажатые левой рукой: {left_count_vyzov_tri}")
    print(f"Удобные триграммы, нажатые левой рукой: {left_vyzov_tri}")
    print(f"Триграммы, нажатые правой рукой: {right_count_vyzov_tri}")
    print(f"Удобные триграммы, нажатые левой рукой: {right_vyzov_tri}")
    lv = [left_count_qwerty, left_qwerty,
          right_count_qwerty, right_qwerty,
          left_count_qwerty_tri, left_qwerty_tri,
          right_count_qwerty_tri, right_qwerty_tri]
    rv = [left_count_vyzov, left_vyzov,
          right_count_vyzov, right_vyzov,
          left_count_vyzov_tri, right_vyzov_tri,
          right_count_vyzov_tri, left_vyzov_tri]
    vyvod_gistogramma4(lv, rv)
