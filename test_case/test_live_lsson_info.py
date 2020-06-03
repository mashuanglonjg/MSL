'''
@Time  : 2020/6/1 10:05
@Author: fengzhj
@doc   : 
'''

from page.login import Loginpage
import allure

@allure.feature('乐桃学院-发布直播课、排课')
class TestLive_lesson_info():

    def test_live_lesson_info_save(self,browser):
        """创建课程保存并退出，断言名称和课程总价"""
        course_name = 'UI自动化测试'
        num = '101'
        money = '99'
        lesson_page = Loginpage(browser).admin_login('18888888888', 'test1234').create_course()
        course_page = lesson_page.save_course_info(course_name, num, money)
        course_page.search_course(course_name)
        assert '￥' + str(int(num) * int(money)) == course_page.get_course_money()
        assert course_name == course_page.get_course_name()
        assert '直播课' == course_page.get_course_type()

    def test_add_lesson(self, browser):
        """排课"""
        course_name = '11111'
        class_name = '123'
        teacher_name = ''
        course_manger_page = Loginpage(browser).admin_login('18888888888', 'test1234').course_manger()
        course_manger_page.search_course(course_name)
        add_class_page = course_manger_page.goon_edit()
        add_class_page.add_class(class_name, teacher_name)
        assert add_class_page.get_teacher() == teacher_name
        assert add_class_page.get_lesson_name() == class_name
