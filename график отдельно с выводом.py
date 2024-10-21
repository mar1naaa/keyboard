"""
вывод гистограммы 
названия столбцов - имя пальца
разные цвета столбцов - разные пальцы
разная яркость столбцов с одним значением - значение кол-ва нажатий одного пальца для двух разных раскладок

"""


import matplotlib.pyplot as plt
import numpy as np

def vyvod_gistogramma(layout1, layout2):
    """
    Функция для построения горизонтальной гистограммы с количеством нажатий пальцами
    для двух раскладок клавиатуры.

    - layout1: количество нажатий для йцукен
    - layout2: количество нажатий для вызов
    """
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)', 'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    index = np.arange(len(fingers))
    bar_width = 0.35

    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width/2, layout1[i], bar_width, label='Йцукен' if i == 0 else "", color=colors[i], alpha=0.7)
        plt.barh(index[i] + bar_width/2, layout2[i], bar_width, label='Вызов' if i == 0 else "", color=colors[i], alpha=1.0)

    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.title('Сравнение нагрузок на пальцы в раскладках йцукен и вызов')
    plt.yticks(index, fingers)


    plt.legend()


    plt.tight_layout()
    plt.show()

# Пример использования функции:

layout1 = [50, 30, 20, 40, 10, 45, 35, 25, 30, 15]
layout2 = [55, 25, 15, 35, 20, 40, 30, 20, 25, 10] 


# Вызов функции для построения графика
plot_finger_usage(layout1, layout2)