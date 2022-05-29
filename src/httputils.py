# @Date: 2022/5/29
# @Author: wkq

import json

import requests


def get(url, data=None, headers=None):
    try:
        response = requests.api.get(url, params=data, headers=headers, verify=False)
        return response
    except Exception as e:
        print(e)


def post(url, data=None, headers=None):
    try:
        params = None if not data else json.dumps(data) if headers["Content-Type"] == 'application/json' else data
        response = requests.api.post(url=url, data=params, headers=headers, verify=False)
        return response
    except Exception as e:
        print(e)
