
import re
from common.conifg import myconf


# class ConText:
#     """用来（临时）保存接口之间依赖参数的类"""
#     pass





def data_replace(data):
    """替换动态参数"""
    while re.search(r'#(.+?)#',data):
        res = re.search(r'#(.+?)#',data)
        # 提取要替换的内容
        r_data = res.group()
        # 获取要替换的字段
        key = res.group(1)
        # 去配置文件中读取字段对应的数据
        try:
            value = myconf.get('data',key)
        except:
            print('数据不存在')
            # value = getattr(ConText,key)

        # 进行替换
        data = re.sub(r_data,str(value),data)
    return data












