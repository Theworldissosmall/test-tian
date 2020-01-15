"""
==========================================
author:田剑锋
file: config.py
time: 2019/09/2019/9/21/11:20
E-mail:tianjianfeng1995@163.com
==========================================
"""

from configparser import ConfigParser


class MyConfig(ConfigParser):
    """读取配置文件的类"""
    def __init__(self):
        super().__init__()

        # 初始化的时候，打开配置文件
        self.read('/Users/tianjianfeng/Desktop/自动化测试/自动化项目/Simplify/conf/conf.ini',encoding='utf8')

myconf = MyConfig()


