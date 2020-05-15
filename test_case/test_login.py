'''
@Time  : 2020/4/28 15:04
@Author: fengzhj
@doc   : 
'''
from conftest import browser
import pytest
from page.login import Loginpage
import allure
import time

@allure.feature('乐桃学院')
class TestLogin():
    login_page = Loginpage(browser)
    def test_findpwd(self,browser):
        """找回密码"""
        login_page = Loginpage(browser)
        login_page.findpwd()
        assert '重置密码' in login_page.get_findpwd_title()
        login_page.back()

    def test_service(self,browser):
        """检查服务协议内容"""
        login_page = Loginpage(browser)
        login_page.service()
        assert '乐桃学院服务协议' in login_page.get_service_title()
        assert 'hello world' in login_page.get_service_text()
        login_page.service_quit()

    def test_login(self,browser):
        """登录"""
        login_page = Loginpage(browser)
        login_page.login('955112', 'test1234')

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])