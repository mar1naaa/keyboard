"""
Лабораторная №1
Считывает количество нажатий
каждым пальцем
в различных раскладках
"""

from function import count_finger_load_dictor, \
    count_finger_load_qwerty, count_finger_load_scoropis, \
    count_finger_load_vyzov, load_hand_left, \
    load_hand_right, vyvod_gistogramma
if __name__ == "__main__":
    with open('full_text.txt', "r", encoding='utf-8') as f:
        text = f.read()

    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)
    dictor_finger_load = count_finger_load_dictor(text)
    scoropis_finger_load = count_finger_load_scoropis(text)
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
    vyvod_gistogramma(qwerty_finger_load,
                      vyzov_finger_load, dictor_finger_load,
                      scoropis_finger_load)
