'''
@Time  : 2020/6/2 15:31
@Author: fengzhj
@doc   : 添加学员名单页面
'''

from poium import Page, PageElement
import time

class AddStu_page(Page):
    lekeno_loc = PageElement(xpath='//input[@class="ant-input"]')  # 输入乐号
    add_bt = PageElement(xpath='//span[text()="添加"]')  # 添加
    back_bt = PageElement(xpath='//span[text()="取消"]')  # 取消，返回上一层

    def add_stu(self,lekeno):
        self.lekeno_loc = lekeno
        self.add_bt.click()
        time.sleep(1)
        self.back_bt.click()