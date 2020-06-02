'''
@Time  : 2020/6/1 16:19
@Author: fengzhj
@doc   : 直播课上课名单
'''

from poium import Page, PageSelect, PageElement
import time

class Name_list_page(Page, PageSelect):

    add_stu_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/span')  # 添加学员
    add_stus_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span')  # 批量导入
    search_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/span')  # 查询
    name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/input')  # 姓名
    phone_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/input')  # 手机号

    def add_stu(self):
        """单个添加学员"""
        self.add_stu_bt.click()
