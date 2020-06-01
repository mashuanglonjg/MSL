'''
@Time  : 2020/5/30 16:31
@Author: fengzhj
@doc   : 直播课信息页面
'''

from poium import Page, PageSelect, PageElement
from datetime import date, timedelta
from page.course_manger import Coursemanger_page
import time

class Live_lesson_page(Page, PageSelect):

    create_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/span')  # 创建课程按钮
    create_live_bt = PageElement(name='live-lesson')  # 创建直播课
    create_demand_bt = PageElement(name='on-demand-lesson')  # 创建点播课
    course_name_loc = PageElement(name='courseName')  # 课程名称
    start_date_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/span[1]/div/input')  # 开始时间
    end_date_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/span[2]/div/input')  # 结束时间
    start_date1_loc = PageElement(xpath='/html/body/div[4]/div/div/div/div/div[1]/div/input')
    end_date1_loc = PageElement(xpath='/html/body/div[5]/div/div/div/div/div[1]/div/input')
    class_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[3]/div/div[1]/span')  # 分类
    class1_loc = PageElement(xpath='/html/body/div[6]/div/div/div/ul/li')  # 一级分类
    class2_loc = PageElement(xpath='/html/body/div[6]/div/div/div/ul[2]/li[3]')  # 二级分类
    num_loc = PageElement(name='count')  # 课时数
    money_loc = PageElement(name='unitPrice')  # 单价
    info_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[9]/div/div[1]')  # 课程介绍
    save_bt = PageElement(name='saveBtn')  # 保存
    next_bt = PageElement(name='nextBtn')  # 下一步

    def save_course_info(self, course_name, num, money):
        """创建直播课\输入课程信息保存"""
        self.create_bt.click()
        time.sleep(1)
        self.create_live_bt.click()
        time.sleep(1)
        start_time = date.today().strftime("%Y-%m-%d")
        end_time = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")
        self.course_name_loc = course_name
        self.start_date_loc.click()
        self.start_date1_loc = start_time
        self.end_date_loc.click()
        self.end_date1_loc = end_time
        self.class_loc.click()
        self.class1_loc.click()
        self.class2_loc.click()
        self.num_loc = num
        self.money_loc = money
        self.info_loc.click()
        self.save_bt.click()
        return Coursemanger_page(self.driver)


