'''
@Time  : 2020/5/15 15:54
@Author: fengzhj
@doc   : 添加老师页面
'''

from poium import Page, PageElement
import time

class AddTc_page(Page):
    add_teacher_title_loc = PageElement(xpath='//span[text()="添加老师"]')  # 添加老师页签，用于断言
    LoginName_loc = PageElement(xpath='(//input[@class="ant-input"])[1]')  # 乐号
    Name_loc = PageElement(xpath='(//input[@class="ant-input"])[2]')  # 姓名
    Content_loc = PageElement(xpath='(//div[@class="lumte-teacher-textarea"])')  # 简介
    add_bt = PageElement(xpath='//span[text()="添加"]')  # 提交按钮
    add1_bt = PageElement(name='sureBtn')  # 确认
    name_loc = PageElement(xpath='(//td[@class="ant-table-row-cell-break-word"])[1]')  # 结果中的姓名

    def get_add_title(self):
        return str(self.add_teacher_title_loc.text)

    def add_teacher(self,LoginName,Name,Content):
        """增加单个老师"""
        self.LoginName_loc = LoginName
        self.Name_loc = Name
        self.Content_loc = Content
        self.add_bt.click()
        self.add1_bt.click()

    def get_tc_name(self):
        """获取添加的老师名字"""
        return str(self.name_loc.text)



