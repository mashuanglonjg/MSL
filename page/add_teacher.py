'''
@Time  : 2020/5/15 15:54
@Author: fengzhj
@doc   : 添加老师页面
'''

from poium import Page, PageElement

class AddTc_page(Page):
    LoginName_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/input')  # 乐号
    Name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/div/input')  # 姓名
    Content_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div/textarea')  # 简介
    add_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/span')  # 提交按钮
    add1_bt = PageElement(xpath='/html/body/div[4]/div/div[2]/div[2]/span')  # 确认

    def add_teacher(self,LoginName,Name,Content):
        """增加单个老师"""
        self.LoginName_loc = LoginName
        self.Name_loc = Name
        self.Content_loc = Content
        self.add_bt.click()
        self.add1_bt.click()

