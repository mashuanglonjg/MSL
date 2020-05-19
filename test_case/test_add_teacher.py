'''
@Time  : 2020/5/18 15:00
@Author: fengzhj
@doc   : 
'''

from conftest import browser
import pytest
from page.login import Loginpage
from page.admin_manger import Adminpage
import allure
import time

@allure.feature('乐桃学院-添加老师')
class TestAddTC():

    def test_addpage(self,browser):
        """是否进入添加老师页面"""
        add_page = Loginpage(browser).admin_login('18888888888', 'test1234').add_tc()
        assert '添加老师' == add_page.get_add_title()

    def test_add_tc(self,browser):
        """单个添加老师"""
        # add_page = Loginpage(browser).admin_login('2512759', 'test1234').add_tc()
        add_page = Loginpage(browser).admin_login('18888888888', 'test1234').add_tc()
        add_page.add_teacher('18877777777', '自动化测试', '这是UI自动化数据, 这是UI自动化数据')
        assert '自动化测试' == add_page.get_tc_name()

    def test_add_tcs(self,browser):
        """批量添加老师"""
        pass


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_add_teacher.py"])