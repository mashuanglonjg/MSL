'''
@Time  : 2020/5/27 14:59
@Author: fengzhj
@doc   : 
'''

from conftest import browser
from page.login import Loginpage
from page.admin_manger import Adminpage
import allure

@allure.feature('乐桃学院-课程管理')
class TestCourse_manger():

    def test_search_course(self, browser):
        """查询课程"""
        course_page = Loginpage(browser).admin_login('18888888888', 'test1234').course_manger()
        course_page.search_lesson()

    def test_create_live(self, browser):
        """创建直播课"""
        course_page = Loginpage(browser).admin_login('18888888888', 'test1234').course_manger()
        course_page.creat_live()