'''
@Time  : 2020/5/15 16:39
@Author: fengzhj
@doc   : 
'''

from conftest import browser
import pytest
from page.login import Loginpage
import allure
import time

@allure.feature('乐桃学院-老师管理')
class TestTM():

    def test_TM_page(self,browser):
        self.tm_page = Loginpage(browser).login('955112', 'a1234567').task()
        self.task_page.do_task()
        #断言已完成角标存在
        assert 5 == self.task_page.get_len()

    def test_login(self,browser):
        """登录"""
        login_page = Loginpage(browser)
        login_page.login('955112', 'test1234')

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_teacher_manger.py"])