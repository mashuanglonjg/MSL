'''
@Time  : 2020/5/30 16:31
@Author: fengzhj
@doc   : 直播课信息页面
'''

from poium import Page, PageSelect, PageElement
import time

class Live_lesson_page(Page, PageSelect):

    course_name_loc = PageElement(name='courseName')  # 课程名称
    start_date_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/span[1]/div/input')  # 开始时间
    end_date_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/span[2]/div/input')  # 结束时间
    start_date1_loc = PageElement(xpath='/html/body/div[4]/div/div/div/div/div[1]/div/input')
    end_date1_loc = PageElement(xpath='/html/body/div[5]/div/div/div/div/div[1]/div/input')
    class_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[3]/div/div[1]/span/input')  # 分类
    num_loc = PageElement(name='count')  # 课时数
    money_loc = PageElement(name='unitPrice')  # 单价
    info_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[9]/div/div[1]')  # 课程介绍
    save_bt = PageElement(name='saveBtn')  # 保存
    next_bt = PageElement(name='nextBtn')  # 下一步

    def save_course_info(self):
        """输入课程信息保存"""
        self.course_name_loc = '123'
        self.start_date_loc.click()
        time.sleep(2)
        self.start_date1_loc = '2020-06-01'
        time.sleep(2)
        self.end_date_loc.click()
        time.sleep(2)
        self.end_date1_loc = '2020-06-05'
        time.sleep(5)