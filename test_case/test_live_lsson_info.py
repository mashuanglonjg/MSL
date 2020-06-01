'''
@Time  : 2020/6/1 10:05
@Author: fengzhj
@doc   : 
'''

from page.login import Loginpage
import allure

@allure.feature('乐桃学院-课程管理')
class TestLive_lesson_info():

    def test_live_lesson_info_save(self,browser):
        course_page = Loginpage(browser).admin_login('18888888888', 'test1234').course_manger()
        lesson_page = course_page.creat_live()
        lesson_page.save_course_info()

