'''
@Time  : 2020/5/18 11:46
@Author: fengzhj
@doc   : 机构管理员管理页面
'''

from poium import Page, PageElement
from page.teacher_manger import Teacher_mangerpage
from page.add_teacher import AddTc_page
import time

class Adminpage(Page):
    home_page_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[1]/ul/li[1]/div')  # 导航栏首页
    school_manger_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[1]/ul/li[2]/div/div/span')  # 教学教务
    teacher_manger_bt = PageElement(xpath='//*[@id="2$Menu"]/li/div/span')  # 老师管理
    add_teacher_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/span')  # 添加老师
    add_teacher_all_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/span')  # 批量添加老师

    def tc_manger(self):
        # self.school_manger_bt.click()  # 默认打开了导航栏

        self.teacher_manger_bt.click()
        time.sleep(1)
        return Teacher_mangerpage(self.driver)

    def add_tc(self):
        # self.school_manger_bt.click()  # 默认打开了导航栏

        self.teacher_manger_bt.click()
        time.sleep(1)
        self.add_teacher_bt.click()
        time.sleep(1)
        return AddTc_page(self.driver)