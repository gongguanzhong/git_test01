# coding:utf-8
import unittest
import HTMLTestRunner
import time

# 给文件名添加当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def all_case():
    # 待执行的目录
    case_dir = "./case1"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
    testcase.addTests(discover)  # 直接加载discover
    print(testcase)
    return testcase


if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    report_path = "./report//" + now + 'result.html'
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'这是我的测试报告', description=u'用例执行情况：')
    # 返回所有用例
    runner.run(all_case())
    fp.close()
