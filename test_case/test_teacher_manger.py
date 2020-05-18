'''
@Time  : 2020/5/15 16:39
@Author: fengzhj
@doc   : 教师管理页面相关用例
'''

from conftest import browser
import pytest
from page.login import Loginpage
from page.admin_manger import Adminpage
import allure
import time

@allure.feature('乐桃学院-老师管理')
class TestTM():

    def test_TM_page(self,browser):
        """是否进入老师管理页面"""
        tm_page = Loginpage(browser).admin_login('2512759', 'test1234').tc_manger()
        assert '老师管理' == tm_page.get_tcmangertitle()

    def test_TM_phone(self,browser):
        """查找号码"""
        phone = '18888888888'
        tm_page = Loginpage(browser).admin_login('2512759', 'test1234').tc_manger()
        tm_page.find_teacher_phone(phone)
        assert phone == tm_page.get_phone()

    def test_TM_name(self,browser):
        """查找姓名"""
        name = '冯忠杰'
        tm_page = Loginpage(browser).admin_login('2512759', 'test1234').tc_manger()
        tm_page.find_name_loc(name)
        assert name ==tm_page.get_name()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_teacher_manger.py"])