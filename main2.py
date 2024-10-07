# 5 Вращение правильной четырехугольной пирамиды относительно оси, проходящей через одну из ее вершин.
# Ось вращения не совпадает с координатными осями.

import numpy as np
import matplotlib.pyplot as plt
import time


# Функция для создания вершин правильной четырехугольной пирамиды
def get_pyramid_vertices(base_size, height):
    half_base = base_size / 2
    return np.array([
        [0, 0, height, 1],  # Вершина
        [-half_base, -half_base, 0, 1],  # Вершина 1
        [half_base, -half_base, 0, 1],  # Вершина 2
        [half_base, half_base, 0, 1],  # Вершина 3
        [-half_base, half_base, 0, 1]  # Вершина 4
    ])


# Функция для вращения точки вокруг оси
def rotate_point(point, angle, axis):
    angle_rad = np.radians(angle)
    axis = axis / np.linalg.norm(axis)

    c = np.cos(angle_rad)
    s = np.sin(angle_rad)
    t = 1 - c

    x, y, z = axis

    rotation_matrix = np.array([
        [t * x * x + c, t * x * y - s * z, t * x * z + s * y, 0],
        [t * x * y + s * z, t * y * y + c, t * y * z - s * x, 0],
        [t * x * z - s * y, t * y * z + s * x, t * z * z + c, 0],
        [0, 0, 0, 1]
    ])

    point = point - np.array([0, 0, in_height, 0])
    point = np.dot(rotation_matrix, point)
    point = point + np.array([0, 0, in_height, 0])

    return point


# Параметры пирамиды
in_base_size = 2
in_height = 3

# Получаем вершины пирамиды
pyramid_vertices = get_pyramid_vertices(in_base_size, in_height)

# Ось вращения (проходит через вершину)
rotation_axis = np.array([1, 1, 0])  # Вектор оси вращения

# Скорость вращения (градусов в секунду)
rotation_speed = 35

# Создание фигуры и осей
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 5])
ax.view_init(30, 60)

while True:
    # Вычисляем угол поворота в градусах
    in_angle = time.time() * rotation_speed % 360

    # Вращаем все вершины пирамиды, кроме верхней
    rotated_vertices = np.array([rotate_point(vertex, in_angle, rotation_axis) if i != 0
                                 else vertex for i, vertex in enumerate(pyramid_vertices)])

    # Очищаем оси перед отрисовкой нового кадра
    ax.cla()

    # Устанавливаем границы и вид
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([0, 5])
    ax.view_init(30, 60)

    # Рисуем рёбра пирамиды
    ax.plot3D(rotated_vertices[[0, 1], 0], rotated_vertices[[0, 1], 1], rotated_vertices[[0, 1], 2], 'green')
    ax.plot3D(rotated_vertices[[0, 2], 0], rotated_vertices[[0, 2], 1], rotated_vertices[[0, 2], 2], 'green')
    ax.plot3D(rotated_vertices[[0, 3], 0], rotated_vertices[[0, 3], 1], rotated_vertices[[0, 3], 2], 'green')
    ax.plot3D(rotated_vertices[[0, 4], 0], rotated_vertices[[0, 4], 1], rotated_vertices[[0, 4], 2], 'green')

    # Рисуем основание пирамиды
    ax.plot3D(rotated_vertices[1:5, 0], rotated_vertices[1:5, 1], rotated_vertices[1:5, 2], 'green')
    ax.plot3D([rotated_vertices[1, 0], rotated_vertices[4, 0]], [rotated_vertices[1, 1], rotated_vertices[4, 1]],
              [rotated_vertices[1, 2], rotated_vertices[4, 2]], 'green')

    plt.draw()
    plt.pause(0.05)  # Пауза для имитации анимации
