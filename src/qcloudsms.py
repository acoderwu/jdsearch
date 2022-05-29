# @Date: 2022/5/29
# @Author: wkq

import logging

from qcloudsms_py import SmsSingleSender


# 腾讯云短信发送服务
class QCloudSMS(object):
    def __init__(self, phones, message, appid, app_key, sign, tmpl_id):
        self.phones = phones
        # 正文模板填充
        self.message: list = message
        # AppId
        self.appid = appid
        # App Key
        self.app_key = app_key
        # 签名内容
        self.sign = sign
        # 模板 id
        self.tmpl_id = tmpl_id

    def send_msg(self):
        sender = SmsSingleSender(self.appid, self.app_key)
        for phone in self.phones:
            rzb = sender.send_with_param(86, phone, self.tmpl_id, self.message, sign=self.sign, extend='', ext='')
            logging.info("短信发送完成")
            logging.info(rzb)
