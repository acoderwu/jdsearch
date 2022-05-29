# @Date: 2022/5/29
# @Author: wkq

import datetime
import logging
import sys

from config import config
from jdsearch import JdSearch
from qcloudsms import QCloudSMS
from schedule import Schedule


def search():
    param = config.get_config().get("param", None)
    if not param or not param["keyword"]:
        logging.error("关键字为空")
        raise Exception("关键字为空")
    jd = JdSearch(param)
    jd.search()
    find = jd.get_find()
    tip = "错误" if find is None else "上架了" if find else "未上架"
    logging.debug(tip)
    if find:
        now = datetime.datetime.now().__format__("%H:%M")
        phones = config.get_config().get("phones", [])
        if not phones:
            logging.error("手机号错误")
            raise Exception("手机号错误")
        message = [param["keyword"], now]
        appid = config.get_config().get("appid", "")
        app_key = config.get_config().get("app_key", "")
        sign = config.get_config().get("sign", "")
        tmpl_id = config.get_config().get("tmpl_id", "")
        sendmsg = QCloudSMS(phones, message, appid, app_key, sign, tmpl_id)
        sendmsg.send_msg()
        logging.debug("搜索完成")
        raise Exception(tip)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    config_file_list = []
    for index in range(0, len(sys.argv)):
        if index != 0:
            config_file_list.append(sys.argv[index])
    config_file = "config.yml" if not config_file_list else config_file_list[0]
    config.load_config(config_file)
    logging.debug("读取到配置: \n" + config.get_config().__str__())
    Schedule(5, search).do()
