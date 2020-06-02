'''
@Time  : 2020/6/2 15:31
@Author: fengzhj
@doc   : 添加学员名单页面
'''

from poium import Page, PageElement
import time

class AddStu_page(Page):
    lekeno_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input')  # 输入乐号
    add_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/span')  # 添加
    back_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/span')  # 取消，返回上一层

    def add_stu(self,lekeno):
        self.lekeno_loc = lekeno
        self.add_bt.click()
        time.sleep(1)
        self.back_bt.click()