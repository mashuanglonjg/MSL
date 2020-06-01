'''
@Time  : 2020/5/27 14:00
@Author: fengzhj
@doc   : 课程管理页面
'''

from poium import Page, PageSelect, PageElement
from page.live_lesson_info import Live_lesson_page
import time

class Coursemanger_page(Page, PageSelect):

    create_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/span')  # 创建课程按钮
    create_live_bt = PageElement(name='live-lesson')  # 创建直播课
    create_demand_bt = PageElement(name='on-demand-lesson')  # 创建点播课
    search_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[4]/span')  # 查找按钮
    search_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/input')  # 搜索课程名字
    search_type_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]')  # 搜索类型
    search_type1_loc = PageElement(xpath='/html/body/div[4]/div/div/div/ul/li[2]')
    search_status_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[3]/div/div/div/div')  # 搜索状态

    course_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div'
                                       '/div/div/div/div/table/tbody/tr/td[1]/div/div[2]/p[1]')  # 搜索结果中的课程名字
    course_no_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div'
                                           '/div/div/div/div/div[2]/div/p')  # 没有搜索结果的文案
    course_type_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div'
                                       '/div/div/div/div/table/tbody/tr/td[4]')  # 搜索结果中的课程类型
    course_status_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/'
                                         'div/div/div/div/table/tbody/tr/td[5]')  # 搜索结果中的课程状态
    create_lesson_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div'
                                         '/table/tbody/tr/td[6]/div/span[1]')  # 排课
    stu_name_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table'
                                    '/tbody/tr/td[6]/div/span[2]')  # 上课名单
    modif_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody'
                                 '/tr/td[6]/div/span[3]')  # 修改
    share_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/'
                                 'tbody/tr/td[6]/div/span[4]')  # 分享
    up_down_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table'
                                   '/tbody/tr/td[6]/div/span[5]')  # 上下架
    go_edit_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div/div/div/table'
                                   '/tbody/tr[1]/td[6]/div/span[1]')  # 继续编辑
    del_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div/div/div/table/'
                               'tbody/tr[1]/td[6]/div/span[2]')  # 删除

    def creat_live(self):
        """创建直播课"""
        self.create_bt.click()
        time.sleep(1)
        self.create_live_bt.click()
        time.sleep(1)
        return Live_lesson_page(self.driver)

    def search_course(self, course_name):
        """查找已发布的直播课"""
        self.search_name_loc = course_name
        time.sleep(1)
        self.search_type_loc.click()
        print(str(self.search_type1_loc.text))
        self.search_bt.click()

    def del_course(self):
        """删除直播课"""
