"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""
import dict_finger
import matplotlib.pyplot as plt
import numpy as np
from dict_finger import keyboard_finger_qwerty, \
    keyboard_finger_dictor_dop, keyboard_finger_dictor, \
    keyboard_finger_qwerty_dop, keyboard_finger_scoropis, \
    keyboard_finger_scoropis_dop, keyboard_finger_vyzov, \
    keyboard_finger_vyzov_dop, vyzov_finger_count, \
    dictor_finger_count, qwerty_finger_count, \
    scoropis_finger_count, penalty_table_qwerty, \
    penalty_table_qwerty_dop, penalty_table_vyzov,\
    penalty_table_vyzov_dop, count_penalty_qwerty,\
    count_penalty_vyzov


def find_finger(character, keyboard_layout):
    """
        Определяет, какой палец используется
        для набора данного символа на клавиатуре.
    """
    flag = 0
    for finger_name, characters in keyboard_layout.items():
        if character in characters:
            return finger_name, flag
        else:
            if keyboard_layout == keyboard_finger_vyzov:
                for finger_name, characters \
                        in keyboard_finger_vyzov_dop.items():
                    if character in characters:
                        flag = 1
                        return finger_name, flag
            else:
                if keyboard_layout == keyboard_finger_qwerty:
                    for finger_name, characters \
                            in keyboard_finger_qwerty_dop.items():
                        if character in characters:
                            flag = 1
                            return finger_name, flag
                else:
                    if keyboard_layout == keyboard_finger_dictor:
                        for finger_name, characters \
                                in keyboard_finger_dictor_dop.items():
                            if character in characters:
                                flag = 1
                                return finger_name, flag
                    else:
                        if keyboard_layout == keyboard_finger_scoropis:
                            for finger_name, characters \
                                    in keyboard_finger_scoropis_dop.items():
                                if character in characters:
                                    flag = 1
                                    return finger_name, flag
                                else:
                                    if keyboard_layout == penalty_table_qwerty:
                                        for finger_name, characters in penalty_table_qwerty_dop.items():
                                            if character in characters:
                                                flag = 1
                                                return finger_name, flag
                                            else:
                                                if keyboard_layout == penalty_table_vyzov:
                                                    for finger_name, characters in penalty_table_vyzov_dop.items():
                                                        if character in characters:
                                                            flag = 1
                                                            return finger_name, flag

    else:
        return "Invalid character: {}".format(character), flag


def count_finger_load_qwerty(text):
    """
        Подсчитывает нагрузку на пальцы, использованные при наборе текста
        на клавиатурной раскладке ЙЦУКЕН.
    """
    for character in text:
        finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_qwerty)
        if finger_name in dict_finger.qwerty_finger_count:
            dict_finger.qwerty_finger_count[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5'
                dict_finger.qwerty_finger_count[shift_finger] += 1

    layout_1 = list(qwerty_finger_count.values())
    return layout_1


def count_finger_load_vyzov(text):
    """
        Подсчитывает нагрузку на пальцы,
        использованные при наборе текста
        в раскладке ВЫЗОВ.
    """
    for character in text:
        finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_vyzov)
        alt_finger = 'rfi1'
        if finger_name in dict_finger.vyzov_finger_count:
            dict_finger.vyzov_finger_count[finger_name] += 1
        if character.isupper() or flag_nado == 1:
            shift_finger = 'lfi5'
            dict_finger.vyzov_finger_count[shift_finger] += 1
        if character == '№':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'ц':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'щ':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'ъ':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'ю':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'э':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'Ц':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'Щ':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'Ю':
            dict_finger.vyzov_finger_count[alt_finger] += 1
        if character == 'Э':
            dict_finger.vyzov_finger_count[alt_finger] += 1

    layout_2 = list(vyzov_finger_count.values())
    return layout_2


def count_finger_load_dictor(text):
    """
        Подсчитывает нагрузку на пальцы,
        использованные при наборе текста
        на клавиатурной раскладке ДИКТОР.
    """
    for character in text:
        finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_dictor)
        if finger_name in dict_finger.dictor_finger_count:
            dict_finger.dictor_finger_count[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5'
                dict_finger.dictor_finger_count[shift_finger] += 1

    layout_3 = list(dictor_finger_count.values())
    return layout_3


def count_finger_load_scoropis(text):
    """
        Подсчитывает нагрузку на пальцы, использованные при наборе текста
        на клавиатурной раскладке СКОРОПИСЬ.
    """
    for character in text:
        finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_scoropis)
        if finger_name in dict_finger.scoropis_finger_count:
            dict_finger.scoropis_finger_count[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5'
                dict_finger.scoropis_finger_count[shift_finger] += 1

    layout_4 = list(scoropis_finger_count.values())
    return layout_4


def load_hand_left(list):
    """
        Вычисляет процент нагрузки
        на левую руку на основе значений из переданного списка.
    """
    start_index = 0
    end_index = 5
    start_index_1 = 0
    end_index_1 = 9
    partial_sum = sum(list[start_index:end_index])
    general_sum = sum(list[start_index_1:end_index_1])
    procent = int((partial_sum * 100) / general_sum)
    return procent


def load_hand_right(list):
    """
        Вычисляет процент нагрузки
        на правую руку на основе значений из переданного списка.
    """
    start_index = 5
    end_index = 9
    start_index_1 = 0
    end_index_1 = 9
    partial_sum = sum(list[start_index:end_index])
    general_sum = sum(list[start_index_1:end_index_1])
    procent = int((partial_sum * 100) / general_sum)
    return procent


def clicks(layout_1, layout_2, layout_3, layout_4):
    """
        Выводит количество нажатий на каждый палец
    """
    fing = ['левый мизинец', 'левый безымянный', 'левый средний',
            'левый указательный', 'левый большой',
            'правый большой', 'правый указательный', 'правый средний',
            'правый безымянный', 'правый мизинец']
    fing_d_qwerty = dict(zip(fing, layout_1))
    fing_d_vyzov = dict(zip(fing, layout_2))
    fing_d_dictor = dict(zip(fing, layout_3))
    fing_d_scoropis = dict(zip(fing, layout_4))
    return fing_d_qwerty, fing_d_vyzov, fing_d_dictor, fing_d_scoropis


def count_load_penalty_qwerty(text):
    for character in text:
        finger_name, flag_nado = find_finger(character.lower(), penalty_table_qwerty)
        if finger_name in count_penalty_qwerty:
            count_penalty_qwerty[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5_2'
                count_penalty_qwerty[shift_finger] += 1
    layout_1 = list(count_penalty_qwerty.values())
    layout_1[1] *= 2
    layout_1[4] *= 2
    layout_1[6] *= 2
    layout_1[8] *= 2
    layout_1[13] *= 2
    layout_1[16] *= 2
    layout_1[18] *= 2
    layout_1[20] *= 2
    layout_1[2] *= 3
    layout_1[9] *= 3
    layout_1[14] *= 3
    layout_1[21] *= 3
    layout_1[22] *=4
    layout_1[23] *= 5
    layout_1.pop(-1)
    lfi5 = [0]
    lfi4 = [0]
    lfi3 = [0]
    lfi2 = [0]
    lfi1 = [0]
    rfi5 = [0]
    rfi4 = [0]
    rfi3 = [0]
    rfi2 = [0]
    rfi1 = [0]
    lfi5[0] = layout_1[0] + layout_1[1] + layout_1[2]
    lfi4[0] = layout_1[3] + layout_1[4]
    lfi3[0] = layout_1[5] + layout_1[6]
    lfi2[0] = layout_1[7] + layout_1[8] + layout_1[9]
    lfi1[0] = layout_1[10]
    rfi1[0] = layout_1[11]
    rfi2[0] = layout_1[12] + layout_1[13] + layout_1[14]
    rfi3[0] = layout_1[15] + layout_1[16]
    rfi4[0] = layout_1[17] + layout_1[18]
    rfi5[0] = layout_1[19] + layout_1[20] + layout_1[21] + layout_1[22]+ layout_1[23]
    penalty_qwerty = lfi5 + lfi4 + lfi3 + lfi2 + lfi1+ rfi1 + rfi2 + rfi3 + rfi4 + rfi5
    return penalty_qwerty

def count_load_penalty_vyzov(text):
    for character in text:
        finger_name, flag_nado = find_finger(character.lower(), penalty_table_vyzov)
        if finger_name in count_penalty_vyzov:
            count_penalty_vyzov[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'lfi5_2'
                count_penalty_vyzov[shift_finger] += 1
    layout_2 = list(count_penalty_vyzov.values())
    layout_2[1] *= 2
    layout_2[3] *= 2
    layout_2[5] *= 2
    layout_2[7] *= 2
    layout_2[12] *= 2
    layout_2[15] *= 2
    layout_2[17] *= 2
    layout_2[19] *= 2
    layout_2[8] *= 3
    layout_2[13] *= 3
    layout_2[20] *= 3
    layout_2[21] *= 4
    layout_2.pop(-1)
    lfi5 = [0]
    lfi4 = [0]
    lfi3 = [0]
    lfi2 = [0]
    lfi1 = [0]
    rfi5 = [0]
    rfi4 = [0]
    rfi3 = [0]
    rfi2 = [0]
    rfi1 = [0]
    lfi5[0] = layout_2[0] + layout_2[1]
    lfi4[0] = layout_2[2] + layout_2[3]
    lfi3[0] = layout_2[4] + layout_2[5]
    lfi2[0] = layout_2[6] + layout_2[7] + layout_2[8]
    lfi1[0] = layout_2[9]
    rfi1[0] = layout_2[10]
    rfi2[0] = layout_2[11] + layout_2[12] +layout_2[13]
    rfi3[0] = layout_2[14] + layout_2[15]
    rfi4[0] = layout_2[16] + layout_2[17]
    rfi5[0] = layout_2[18] + layout_2[19] + layout_2[20] + layout_2[21]
    penalty_vyzov = lfi5 + lfi4 + lfi3 + lfi2 + lfi1 + rfi1 + rfi2 + rfi3 + rfi4 + rfi5
    return penalty_vyzov

def proucent_penalty(qwerty, vyzov):
    pr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pr[0] = abs(round(((qwerty[0]-vyzov[0])/((qwerty[0]+vyzov[0])/2))*100))
    pr[1] = abs(round(((qwerty[1]-vyzov[1])/((qwerty[1]+vyzov[1])/2))*100))
    pr[2] = abs(round(((qwerty[2]-vyzov[2])/((qwerty[2]+vyzov[2])/2))*100))
    pr[3] = abs(round(((qwerty[3]-vyzov[3])/((qwerty[3]+vyzov[3])/2))*100))
    pr[6] = abs(round(((qwerty[6]-vyzov[6])/((qwerty[6]+vyzov[6])/2))*100))
    pr[7] = abs(round(((qwerty[7]-vyzov[7])/((qwerty[7]+vyzov[7])/2))*100))
    pr[8] = abs(round(((qwerty[8]-vyzov[8])/((qwerty[8]+vyzov[8])/2))*100))
    pr[9] = abs(round(((qwerty[9]-vyzov[9])/((qwerty[9]+vyzov[9])/2))*100))
    return pr

def vyvod_gistogramma(layout1, layout2, layout3, layout4, layout5, layout6):
    plt.figure(figsize=(10, 6))
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)',
               'Указательный (левая)', 'Большой (левая)',
               'Большой (правая)', 'Указательный (правая)',
               'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
    color1 = ['#ff0033']
    color2 = ['#0000ff']
    color3 = ['#009900']
    color4 = ['#ffcc00']
    index = np.arange(len(fingers))
    bar_width = 0.2
    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width * 1.5, layout4[i], bar_width,
                 label='Скоропись' if i == 0 else "", color=color4,
                 alpha=1.0)
        plt.barh(index[i] - bar_width * 0.5, layout3[i], bar_width,
                 label='Диктор' if i == 0 else "", color=color3,
                 alpha=1.0)
        plt.barh(index[i] + bar_width * 0.5, layout2[i], bar_width,
                 label='Вызов' if i == 0 else "", color=color2,
                 alpha=1.0)
        plt.barh(index[i] + bar_width * 1.5, layout1[i], bar_width,
                 label='Йцукен' if i == 0 else "", color=color1,
                 alpha=1.0)
    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.title('Сравнение нагрузок на пальцы в различных раскладках')
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    plt.yticks(index, fingers)
    plt.legend()
    plt.tight_layout()

    plt.figure(figsize=(10, 6))
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)',
               'Большой (правая)', 'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)',
               'Мизинец (правая)']
    color1 = '#ff0033'
    color2 = '#0000ff'

    index = np.arange(len(fingers))
    bar_width = 0.2

    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width / 2, layout6[i], bar_width, label='Вызов' if i == 0 else "", color=color1,
                 alpha=0.7)
        plt.barh(index[i] + bar_width / 2, layout5[i], bar_width, label='Йцукен' if i == 0 else "", color=color2,
                 alpha=1.0)

    plt.yticks(index, fingers)
    plt.ylabel('Пальцы')
    plt.xlabel('Штрафы (в тысячах)')
    plt.title('Штрафы на пальцы в раскладках ЙЦУКЕН и ВЫЗОВ')

    # Форматируем значения по оси X
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

    plt.legend()
    plt.tight_layout()
    plt.show()
