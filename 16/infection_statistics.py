import csv
import matplotlib.pyplot as plt
import datetime
import CaixinData.caixin_pneumonia_data as cpd

# 更新数据
option = input("更新数据？y/n")
if option == 'y':
    cpd.run()

filename = 'CaixinData/data2.csv'
with open(filename, encoding='utf-8') as f:
    # 计算多少行
    lines = len(f.readlines())

    # 返回第一行，因为readline()执行完后在文件末尾
    f.seek(0)

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
    hubei = []
    for row in reader:
        try:
            total.append(int(row[1]))
            hubei.append(int(row[2]))
        except ValueError:
            print('data missing')


    # 生成一个日期轴
    day_list = ['2019-12-31', '2019-1-11']
    begin = datetime.date(2020, 1, 16)
    for i in range(lines-3):
        day = begin + datetime.timedelta(days=i)
        day_list.append(str(day))

    # 根据数据绘制图形
    fig = plt.figure(dpi=200, figsize=(10,6))

    plt.plot(day_list, total, c='black', linewidth=3)
    plt.plot(day_list, hubei, c='gray', linewidth=3)
    plt.fill_between(day_list, total, hubei, facecolor='blue', alpha=0.1)

    # 设置图形格式
    plt.title("全国和湖北确诊人数", fontsize=24)
    plt.ylabel("Infection Toll", fontsize=16)

    plt.xticks(rotation=90)  # 90为旋转的角度


plt.savefig("result.png", dpi=200, bbox_inches='tight')

plt.show()





