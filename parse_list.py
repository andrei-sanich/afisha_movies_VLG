import re


def parse_list(lst_str):
    return list(map(lambda x: x.strip(),re.sub(r'[\'\{\}]', '', lst_str).split(',')))

