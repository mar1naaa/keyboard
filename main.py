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

from function import count_finger_load_dictor, \
    count_finger_load_qwerty, count_finger_load_scoropis, \
    count_finger_load_vyzov, load_hand_left, \
    load_hand_right, vyvod_gistogramma, count_load_penalty_qwerty, \
    count_load_penalty_vyzov, proucent_penalty, get_hand_and_finger, get_hand_and_finger_1, \
    count_digrams_with_layout, vyvod_gistogramma3
from dict_finger import keyboard_finger_dictor, keyboard_finger_qwerty, keyboard_finger_scoropis, keyboard_finger_vyzov
if __name__ == "__main__":
    with open('digrams.txt', "r", encoding='utf-8') as f:
        text = f.read()
    """"
    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)
    dictor_finger_load = count_finger_load_dictor(text)
    scoropis_finger_load = count_finger_load_scoropis(text)
    penalty_qwerty = count_load_penalty_qwerty(text)
    penalty_vyzov = count_load_penalty_vyzov(text)
    print(qwerty_finger_load)
    print(vyzov_finger_load)
    print(dictor_finger_load)
    print(scoropis_finger_load)
    left_qwerty = load_hand_left(qwerty_finger_load)
    right_qwerty = load_hand_right(qwerty_finger_load)
    left_vyzov = load_hand_left(vyzov_finger_load)
    right_vyzov = load_hand_right(vyzov_finger_load)
    left_dictor = load_hand_left(dictor_finger_load)
    right_dictor = load_hand_right(dictor_finger_load)
    left_scoropis = load_hand_left(scoropis_finger_load)
    right_scoropis = load_hand_right(scoropis_finger_load)
    print('ЙЦУКЕН')
    print('Нагрузка на левую руку в процентах:', left_qwerty, '%')
    print('Нагрузка на правую руку в процентах:', right_qwerty, '%')
    print('ВЫЗОВ')
    print('Нагрузка на левую руку в процентах:', left_vyzov, '%')
    print('Нагрузка на правую руку в процентах:', right_vyzov, '%')
    print('ДИКТОР')
    print('Нагрузка на левую руку в процентах:', left_dictor, '%')
    print('Нагрузка на правую руку в процентах:', right_dictor, '%')
    print('СКОРОПИСЬ')
    print('Нагрузка на левую руку в процентах:', left_scoropis, '%')
    print('Нагрузка на правую руку в процентах:', right_scoropis, '%')
    fing = ['левый мизинец', 'левый безымянный', 'левый средний',
            'левый указательный', 'левый большой',
            'правый большой', 'правый указательный',
            'правый средний', 'правый безымянный', 'правый мизинец']
    fing_d_qwerty = dict(zip(fing, qwerty_finger_load))
    fing_d_vyzov = dict(zip(fing, vyzov_finger_load))
    fing_d_dictor = dict(zip(fing, dictor_finger_load))
    fing_d_scoropis = dict(zip(fing, scoropis_finger_load))
    print('Количество нажатий каждым пальцем в различных раскладках')
    print('ЙЦУКЕН:', fing_d_qwerty)
    print('ВЫЗОВ:', fing_d_vyzov)
    print('ДИКТОР:', fing_d_dictor)
    print('СКОРОПИСЬ:', fing_d_scoropis)
    print('Количество штрафов в раскладке ЙЦУКЕН на каждый палец:', penalty_qwerty)
    print('Количество штрафов в раскладке ВЫЗОВ на каждый палец:', penalty_vyzov)
    proucent = proucent_penalty(penalty_qwerty, penalty_vyzov)
    print('Разница между штрафами в процентах:',proucent)
    print('Вывод:')
    vyvod_gistogramma(qwerty_finger_load,
                      vyzov_finger_load, dictor_finger_load,
                      scoropis_finger_load, penalty_qwerty, penalty_vyzov)
    """
    input_file = 'digrams.txt'
    left_qwerty, right_qwerty = count_digrams_with_layout(input_file, keyboard_finger_qwerty)
    left_vyzov, right_vyzov = count_digrams_with_layout(input_file, keyboard_finger_vyzov)
    left_dictor, right_dictor = count_digrams_with_layout(input_file, keyboard_finger_dictor)
    left_scoropis, right_scoropis = count_digrams_with_layout(input_file, keyboard_finger_scoropis)
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


