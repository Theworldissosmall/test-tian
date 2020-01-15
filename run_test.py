"""
# ================================================
# @name    : Tian
# @Time    : 2019/10/4 下午12:23
# @File    : run_test.py
# @Email   :tianjianfeng1995@163.com
# ================================================
"""
"""
项目启动文件
"""
import time
import  unittest
import os
from test_Basics.HTMLTestRunnerNew import HTMLTestRunner


#获取当前系统的时间，生成字符串
now = time.strftime("%Y-%m-%d_%H_%M_%S")
#创建测试套件
suite = unittest.TestSuite()

#将用例添加到套件中
loader = unittest.TestLoader()
# TestLoader 类中提供的discover（）方法自动识别测试用例
suite.addTest(loader.discover(r'/Users/tianjianfeng/Desktop/自动化测试/自动化项目/Simplify/testcases'))

# 拼接报告的路径
report_file_path = os.path.join(r'/Users/tianjianfeng/Desktop/自动化测试/自动化项目/Simplify/reports','report'+ now +'.html')

#执行用例，生成测试报告
with open(report_file_path,'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='商业化积分接口测试报告',
                            description='商业化接口测试报告',
                            tester='田剑锋')
    runner.run(suite)
