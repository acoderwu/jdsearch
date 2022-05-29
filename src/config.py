# @Date: 2022/5/29
# @Author: wkq

import fileutils


class Config(object):
    def __init__(self):
        self.config = {}

    def load_config(self, file):
        datas = fileutils.load_yml(file)
        self.config = [] if not datas else datas[0]
        self._config_verify()

    def _config_verify(self):
        if not self.config["appid"]:
            raise Exception("appid is empty")
        if not self.config["app_key"]:
            raise Exception("app_key is empty")
        if not self.config["sign"]:
            raise Exception("sign is empty")
        if not self.config["tmpl_id"]:
            raise Exception("tmpl_id is empty")

    def get_config(self):
        return self.config


config = Config()
