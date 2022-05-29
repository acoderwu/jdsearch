# @Date: 2022/5/29
# @Author: wkq

import yaml


def load_yml(path) -> list:
    if not path:
        return []
    with open(path, 'r', encoding="utf-8") as yml_file:
        content = yaml.full_load_all(yml_file.read())
    datas = []
    for data in content:
        datas.append(data)
    return datas
