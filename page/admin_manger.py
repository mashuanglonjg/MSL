'''
@Time  : 2020/5/18 11:46
@Author: fengzhj
@doc   : 机构管理员管理页面
'''

from poium import Page, PageElement
from page.teacher_manger import Teacher_mangerpage

class Adminpage(Page):
    home_page_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[1]/ul/li[1]/div')  # 导航栏首页
    school_manger_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[1]/ul/li[2]/div/div/span')  # 教学教务
    teacher_manger_bt = PageElement(xpath='//*[@id="2$Menu"]/li/div/span')  # 老师管理

    def tc_manger(self):
        self.school_manger_bt.click()
        self.teacher_manger_bt.click()
        return Teacher_mangerpage(self.driver)