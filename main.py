"""
Лабораторная работа №3
Подсчитывает штрафы на пальцы в раскладках ЙЦУКЕН и ВЫЗОВ
"""

from function import vyvod_gistogramma, count_load_penalty_qwerty, \
    count_load_penalty_vyzov, proucent_penalty

if __name__ == "__main__":
    with open('full_text.txt', "r", encoding='utf-8') as f:
        text = f.read()
    penalty_qwerty = count_load_penalty_qwerty(text)
    penalty_vyzov = count_load_penalty_vyzov(text)
    print('Количество штрафов в раскладке'
          ' ЙЦУКЕН на каждый палец:', penalty_qwerty)
    print('Количество штрафов в раскладке'
          ' ВЫЗОВ на каждый палец:', penalty_vyzov)
    proucent = proucent_penalty(penalty_qwerty, penalty_vyzov)
    print('Разница между штрафами в процентах:', proucent)
    vyvod_gistogramma(penalty_qwerty, penalty_vyzov)
