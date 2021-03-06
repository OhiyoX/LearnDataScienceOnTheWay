# pygal 已经删除了i18n，需要导入pygal_maps_world
from pygal_maps_world.i18n import COUNTRIES


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

    # 如果找到指定的国家，返回None
    return None

