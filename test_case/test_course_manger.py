'''
@Time  : 2020/5/27 14:59
@Author: fengzhj
@doc   : 
'''

from page.login import Loginpage
import allure

@allure.feature('乐桃学院-课程管理')
class TestCourse_manger():

    def test_del_live_lesson(self, browser):
        """删除直播课"""
        course_page = Loginpage(browser).admin_login('18888888888', 'test1234').course_manger()
        course_page.search_course('UI自动化测试')
        course_page.del_course()
