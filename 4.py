import HTMLTestRunnerCN
import unittest
from test.app_test.app_uinttest_dome import Settest

if __name__ == '__main__':
    # 实例化测试套件,定义一个测试容器
    suite= unittest.TestSuite()
    # 加载测试用例
    suite.addTest(Settest('test_seting'))

    # 定义测试报告存放路径和报告名称
    with open('app_autotest_HTMLReropt.html', 'wb')as f:
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='APP设置自动化测试报告',
            description='描述'
        )
        #执行测试套用例
        runner.run(suite)

        # 关闭测试报告
        f.close()