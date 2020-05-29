'''
@Time  : 2020/5/29 20:32
@Author: fengzhj
@doc   : 
'''

from conftest import browser
import pytest
from page.login import Loginpage
from page.account_set import Info_page
import allure
import time

@allure.feature('乐桃学院-个人中心账户设置')
class TestAddTC():
    def test_info(self, browser):
        """是否进入个人资料"""
        info_page =  Loginpage(browser).admin_login('18888888888', 'test1234').account_in()
        assert '个人资料' == info_page.get_title()

    def test_nick(self, browser):
        """修改昵称"""
        nick = '昵称测试'
        nick_page = Loginpage(browser).admin_login('18888888888', 'test1234').account_in()
        nick_page.modef_nick(nick)
        assert nick == nick_page.get_nick()
        nick_page.modef_nick('nick')

