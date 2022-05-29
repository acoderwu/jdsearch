# @Date: 2022/5/29
# @Author: wkq

from src import httputils


class JdSearch(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, param):
        self._find = None
        self._url = "https://search.jd.com/search"
        self._param = param
        self._header = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cp-extension-installed": "Yes",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
        }

    def search(self):
        response = httputils.get(url=self._url, data=self._param, headers=self._header)
        page = str(response.content, encoding="utf-8")
        self._find = "抱歉，没有找到" not in page if page else None

    def get_find(self):
        return self._find
