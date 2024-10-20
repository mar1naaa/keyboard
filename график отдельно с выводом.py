import matplotlib.pyplot as plt
import numpy as np

def plot_finger_usage(layout1, layout2):
    """
    Функция для построения горизонтальной гистограммы с количеством нажатий пальцами
    для двух раскладок клавиатуры.

    - layout1: список количества нажатий для йцукен
    - layout2: список количества нажатий для вызов
    """
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)',
           'Большой (правая)', 'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
          '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    # Позиции столбцов на оси Y
    index = np.arange(len(fingers))

    # Ширина столбцов
    bar_width = 0.35

    # Построение горизонтальной гистограммы
    for i in range(len(fingers)):
        plt.barh(index[i] - bar_width/2, layout1[i], bar_width, label='Йцукен' if i == 0 else "", color=colors[i], alpha=0.7)
        plt.barh(index[i] + bar_width/2, layout2[i], bar_width, label='Вызов' if i == 0 else "", color=colors[i], alpha=1.0)

    # Добавление подписей и заголовков
    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.title('Сравнение нагрузок на пальцы в раскладках йцукен и вызов')
    plt.yticks(index, fingers)

    # Легенда
    plt.legend()

    # Показ гистограммы
    plt.tight_layout()
    plt.show()

# Пример использования функции:

layout1 = [50, 30, 20, 40, 10, 45, 35, 25, 30, 15]  # Количество нажатий в первой раскладке
layout2 = [55, 25, 15, 35, 20, 40, 30, 20, 25, 10]  # Количество нажатий во второй раскладке


# Вызов функции для построения графика
plot_finger_usage(layout1, layout2)