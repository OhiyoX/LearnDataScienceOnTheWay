from die import Die
import matplotlib.pyplot as plt
import pygal

# 创建一个D6
die = Die()


#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_vusual.svg')


x_values = list(range(1, 7))
plt.ylim(ymin=15000, ymax=max(frequencies)*1.1)

plt.plot(x_values, frequencies, linewidth=2)
plt.show()