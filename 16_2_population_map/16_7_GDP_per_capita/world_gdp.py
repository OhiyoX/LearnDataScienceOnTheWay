import csv

# pygal 已经删除了i18n，需要导入pygal_maps_world
from pygal_maps_world.i18n import COUNTRIES
from pygal.style import RotateStyle
from pygal_maps_world.maps import World
from pygal.style import Style

def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == "Hong Kong SAR, China":
            return 'hk'
        if country_name == "Korea, Dem. People’s Rep.":
            return 'kp'
        if country_name == "Korea, Rep.":
            return 'kr'
        if country_name == 'Moldova':
            return 'md'
        if country_name == 'Yemen, Rep.':
            return 'ye'
        if country_name == 'Viet Nam':
            return 'vn'
    # 如果找不到指定的国家，返回None
    return None


# 载入csv
filename = 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_713080.csv'

with open(filename, encoding="UTF-8") as f:
    reader = csv.reader(f)

    # 建gdp字典
    new_gdp_list = {}
    for i in range(5):
        ignore = next(reader)
    for row in reader:
        date = 63
        # 当GDP不为空时
        while not row[date]:
            date -= 1
            if date == 4:
                break
        if date != 4:
            code = get_country_code(row[0])
            # 如果code存在
            if code != None:
                new_gdp_list[code] = float(row[date])

# 为国家分组
gdp_1, gdp_2, gdp_3, gdp_4 = {},{},{},{}
for code, gdp in new_gdp_list.items():
    if gdp > 50000:
        gdp_1[code] = gdp
    elif gdp > 10000:
        gdp_2[code] = gdp
    elif gdp > 1000:
        gdp_3[code] = gdp
    else:
        gdp_4[code] = gdp

# 设置颜色
custom_style = Style(colors=('#000066', '#000099', '#0066ff', '#3399ff'))

wm_style = RotateStyle('#000099')
wm = World(style=custom_style)
wm.title = 'GDP per capita (current US$)'
wm.add("GDP > 50000", gdp_1)
wm.add("GDP 50000-10000", gdp_2)
wm.add("GDP 10000-1000", gdp_3)
wm.add("GDP 1000-0", gdp_4)

wm.render_to_file("result.svg")

