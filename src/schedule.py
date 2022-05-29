# @Date: 2022/5/29
# @Author: wkq

from threading import Timer


# 间时执行
class Schedule(object):
    def __init__(self, interval, func):
        self.interval = interval
        self.func = func

    def do(self):
        self.func()
        Timer(5, self.do).start()
