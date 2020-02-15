import csv
import matplotlib.pyplot as plt
import datetime

filename = 'data2.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rcParams['font.serif'] = ['KaiTi']

    """
    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    同时列出数据和数据下标，一般用在 for 循环当中。
    """
    # 获得全国数据
    total = []
    for row in reader:
        total.append(int(row[1]))

    # 生成一个日期轴
    day_list = ['2019-12-31', '2019-1-11']
    begin = datetime.date(2020, 1, 16)
    end = datetime.date(2020, 2, 14)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        day_list.append(str(day))

    fig = plt.figure(dpi=200, figsize=(10,6))

    plt.plot(day_list, total, c='black', linewidth=3)
    plt.title("全国死亡人数", fontsize=24)
    plt.ylabel("Death Toll", fontsize=16)

    plt.xticks(rotation=90)  # 90为旋转的角度


plt.savefig("result.png", dpi=200, bbox_inches='tight')

plt.show()





