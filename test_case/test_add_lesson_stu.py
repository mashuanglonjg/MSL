'''
@Time  : 2020/6/2 15:50
@Author: fengzhj
@doc   : 
'''

from page.login import Loginpage
import allure

@allure.feature('乐桃学院-上课名单管理（添加）')
class TestAdd_stu():

    def test_add_stu(self, browser):
        lekeno = '955112'
        name = 'UI自动化'
        course_page = Loginpage(browser).admin_login('188888xxxx', 'xxxxxxxx').course_manger()
        course_page.search_course(course_name='test123wan')
        add_stu_page = course_page.name_list()
        add_stu_page.add_stu().add_stu(lekeno)
        add_stu_page.search_stu_name(name)
        assert add_stu_page.get_r_name() == name






