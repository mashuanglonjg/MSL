'''
@Time  : 2020/6/1 16:19
@Author: fengzhj
@doc   : 直播课上课名单
'''

from poium import Page, PageSelect, PageElement
from page.add_lesson_stu import AddStu_page
import time

class Name_list_page(Page, PageSelect):

    add_stu_bt = PageElement(xpath='(//span[text()="添加学员"])')  # 添加学员
    add_stus_bt = PageElement(xpath='(//span[text()="批量导入"])')  # 批量导入
    search_bt = PageElement(xpath='(//span[text()="查询"])')  # 查询
    name_loc = PageElement(xpath='(//input[@class="ant-input"])[1]')  # 姓名
    phone_loc = PageElement(xpath='(//input[@class="ant-input"])[2]')  # 手机号
    r_name_loc = PageElement(xpath='(//td[@class="ant-table-row-cell-break-word"])[1]')  # 查找结果中的名字
    remove_loc = PageElement(xpath='(//span[text()="移除"])[1]')  # 移除
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