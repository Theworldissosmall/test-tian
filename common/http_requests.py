"""
# ================================================
# @name    : Tian
# @Time    : 2019/10/4 下午12:24
# @File    : http_requests.py
# @Email   :tianjianfeng1995@163.com
# ================================================
"""

import requests

class HttpRequest(object):

    # 发送请求方法
    def request(self,method,url,data=None,headers=None):
        """GET   get"""
        method = method.lower()
        if method == 'post':
            # 判断是否使用json来传参
            # 注意：data参数转json请求
            return requests.post(url=url, json=data, headers=headers)
        elif method == 'get':
            return requests.get(url=url, params=data, headers=headers)
