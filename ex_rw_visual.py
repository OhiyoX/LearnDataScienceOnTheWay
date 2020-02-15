import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,linewidth=5)

    #   突出起点和终点

    # 隐藏坐标轴
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
