'''
@Time  : 2020/6/2 11:27
@Author: fengzhj
@doc   : 
'''

from page.login import Loginpage
import allure

@allure.feature('乐桃学院-上课名单管理（查询、删除等）')
class TestCourse_manger():

    def test_search_name(self, browser):
        name = ''
        name_list_page = Loginpage(browser).admin_login('188888xxxx', 'xxxxxxxx4').course_manger().name_list()
        name_list_page.search_stu_name(name)

    # def test_search_phone(self, browser):
    #     phone = ''
    #     name_list_page = Loginpage(browser).admin_login('18888xxxxx', 'xxxxxxxx').course_manger().name_list()
    #     name_list_page.search_stu_phone(phone)

    def test_remove_stu(self, browser):
        name = ''
        name_list_page = Loginpage(browser).admin_login('188888xxxx', 'xxxxxxxx').course_manger().name_list()
        name_list_page.search_stu_name(name)
        name_list_page.remove_stu()