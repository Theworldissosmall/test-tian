"""
# ================================================
# @name    : Tian
# @Time    : 2019/10/4 下午12:36
# @File    : test_pointpark.py
# @Email   :tianjianfeng1995@163.com
# ================================================
"""


"""
测试用例模块

"""
import unittest
from test_Basics.ddt import ddt,data
from common.read_excel import ReadExcel
from common.http_requests import HttpRequest
import time
from common.my_sql import ReadSQL
from common.text_replace import data_replace
# from common.conifg import myconf
import random


@ddt
class PointParkTestCase(unittest.TestCase):
    """try积分接口"""
    excel = ReadExcel(r'/Users/tianjianfeng/Desktop/自动化测试/自动化项目/Simplify/data/cases.xlsx', 'pointpark')
    cases = excel.read_data_obj()
    http = HttpRequest()
    db = ReadSQL()

    @data(*cases) #拆分cases，传递给case；
    def test_case_pointpark(self, case):

        # 准备测试用例数据
        url = case.url
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers = eval(case.headers)
        # data = eval(case.data)
        # if '#uid#' in case.data:
        # 替换文件固定参数
        if '#uid#' in case.data:
            case.data = data_replace(case.data)


        #接收随机生成serialNo
        serialNo =self.random_serialNo()
        #替换动态参数
        if '*serialNo*' in case.data:
            case.data = case.data.replace('*serialNo*',serialNo)
            return case.data


        # 判断是否是执行的cancel积分成功用例，
        # if case.title == "cancel积分成功":
        #     serialNo = self.db.find_one(
        #         "SELECT * FROM pointpark.point_activity_info where serialNo='{}' ORDER BY serialNo DESC".format(myconf.get('data','serialNo')))
        #     print(serialNo)
        #         # 将添加的serialNo，保存为临时变量
        #     setattr(ConText, 'serialNo', serialNo[4])

        # 发送请求到接口，获取结果
        response = self.http.request(method=method, url=url, data=eval(case.data),headers=headers)
        # 获取返回的内容
        res = response.json()



        # 比对预期结果和实际结果，断言用例是否通过
        try:

            self.assertEqual(excepted, res)
            if case.checksql:
                db_res = self.db.find_count(case.checksql)
                self.assertEqual(1, db_res)
                print('预期接口请求结果为:{}'.format(db_res))
            print('实际接口请求结果为:{}'.format(res))
            print('预期接口请求结果为:{}'.format(excepted))
            time.sleep(0)
        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=9, value='未通过')
            raise e
        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=9, value='通过')

    def random_serialNo(self):
        '''随机生成serialNo'''
        while True:
            serialNo = "13"
            for i in range(9):
                num = random.randint(1,9)
                serialNo += str(num)

            # 数据库查询serialNo是否存在
            sql = "SELECT * FROM pointpark.point_activity_info where serialNo='{}'".format(serialNo)
            if not self.db.find_count(sql):
                return serialNo


