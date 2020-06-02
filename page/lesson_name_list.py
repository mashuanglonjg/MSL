'''
@Time  : 2020/6/1 16:19
@Author: fengzhj
@doc   : 直播课上课名单
'''

from poium import Page, PageSelect, PageElement
from page.add_lesson_stu import AddStu_page
import time

class Name_list_page(Page, PageSelect):

    add_stu_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/span')  # 添加学员
    add_stus_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span')  # 批量导入
    search_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/span')  # 查询
    name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/input')  # 姓名
    phone_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/input')  # 手机号
    r_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/'
                                   'div/div/div/table/tbody/tr/td[1]')  # 查找结果中的名字
    remove_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div'
                                   '/div/div/table/tbody/tr/td[5]/div/span')  # 移除
    remove1_loc = PageElement(name='remove-ok')  # 二次确认

    def add_stu(self):
        """单个添加学员"""
        self.add_stu_bt.click()
        return AddStu_page(self.driver)

    def search_stu_name(self, name):
        """通过姓名查找学员"""
        self.name_loc = name
        self.search_bt.click()

    def search_stu_phone(self, phone):
        """通过电话查找学员"""
        self.phone_loc = phone
        self.search_bt.click()

    def get_r_name(self):
        """获取结果中的姓名"""
        return str(self.r_name_loc.text)

    def remove_stu(self):
        """移除上课名单"""
        self.remove_loc.click()
        self.remove1_loc.click()