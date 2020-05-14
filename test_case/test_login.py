'''
@Time  : 2020/4/28 15:04
@Author: fengzhj
@doc   : 
'''
from conftest import browser
import pytest
from page.login import Loginpage
import allure

@allure.feature('demo')
class TestLogin():
    login_page = Loginpage(browser)
    def test_findpwd(self,browser):
        """找回密码"""
        login_page = Loginpage(browser)
        login_page.findpwd()
        assert '重置密码' in login_page.get_findpwd_title()
        login_page.back()

    
    def test_login(self,browser):
        """登录"""
        login_page = Loginpage(browser)
        login_page.login('955112', 'test1234')



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_demo.py"])