"""
# ================================================
# @name    : Tian
# @Time    : 2019/11/19 下午9:18
# @File    : data_replace.py
# @Email   :tianjianfeng1995@163.com
# ================================================
"""

import re
from common.conifg import myconf



def data_replaces(data):
    print(12345)
    """替换动态参数"""
    while re.search(r"#(.+?)#",data):
        res = re.search(r"#(.+?)#",data)
        # 提取要替换的内容
        r_data = res.group()
        print(r_data)
        # 获取要替换的字段
        key = res.group(1)
        print(key)
        # 配置文件中读取字段对应的数据
        value = myconf.get(data,key)
        print(value)
        # 进行替换
        data = re.sub(r_data,str(value),data)
        print(data)

        return data
# if __name__ =='__main':












#
# def data_replaces(data):
#     """替换动态参数"""
#     while re.search(r"#(.+?)#",data):
#         res = re.search(r"#(.+?)#",data)
#         # 提取要替换的内容
#         r_data = res.group()
#         print(r_data)
#         # 获取要替换的字段
#         key = res.group(1)
#         print(key)
#         # 配置文件中读取字段对应的数据
#         value = os.path.join('')
#         print(value)
#         # 进行替换
#         data = re.sub(r_data,str(value),data)
#         print(data)
#
#         return data
#
#
#


# class ConText:
#     """用来（临时）保存接口之间依赖参数的类"""
#     pass
#
#
#
#
#
# def data_replace(data):
#     """替换动态参数"""
#     while re.search(r'#(.+?)#',data):
#         res = re.search(r'#(.+?)#',data)
#         # 提取要替换的内容
#         r_data = res.group()
#         # 获取要替换的字段
#         key = res.group(1)
#         # 去配置文件中读取字段对应的数据
#         try:
#             value = myconf.get('data',key)
#         except:
#             value = getattr(ConText,key)
#         # 进行替换
#         data = re.sub(r_data,str(value),data)
#
#     return data



















