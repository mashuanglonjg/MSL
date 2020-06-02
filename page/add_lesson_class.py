'''
@Time  : 2020/6/2 16:34
@Author: fengzhj
@doc   : 排课
'''

from poium import Page, PageElement
import datetime
import time

class AddLesson_class(Page):
    add_class_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div/span')  # 排课
    pub_lesson_bt = PageElement(name='nextBtn')  # 发布课程
    class_name_loc = PageElement(xpath='//*[@id="ccp-custom-mask"]/div/div[2]/div/div[1]/div[2]/div[1]/div/input')  # 课时名称
    teacher_loc = PageElement(xpath='//*[@id="ccp-custom-mask"]/div/div[2]/div/div[2]/div[2]'
                                    '/div[1]/div/div/div/div/div[1]')  # 授课老师
    start_time_loc = PageElement(xpath='//*[@id="ccp-custom-mask"]/div/div[2]/div/div[3]'
                                     '/div[2]/div[1]/div/span/div/input')  # 课程开始时间
    save_class_bt = PageElement(xpath='//*[@id="ccp-custom-mask"]/div/div[3]/div[2]')  # 确定
    lesson_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]'
                                        '/div/div/div/div/div/div/table/tbody/tr/td[1]')  # 课时名称
    teacher_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]'
                                         '/div/div/div/div/div/div/table/tbody/tr/td[2]')  # 老师名字
    modif_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/'
                                 'div/div/div/div/div/table/tbody/tr/td[6]/div/span[1]')  # 修改
    remove_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div/'
                                  'div/div/div/div/table/tbody/tr/td[6]/div/span[2]')  # 删除
    remove1_bt = PageElement(xpath='/html/body/div[8]/div/div/div/div[2]/div/div/div/div[2]/div[2]/span')  # 二次确认
    modif_class_loc = PageElement(xpath='//*[@id="ccp-custom-mask"]/div/div[2]/div/div[1]'
                                        '/div[2]/div[1]/div/input')  # 修改课程名字
    save_class1_bt = PageElement(xpath='//*[@id="ccp-custom-mask"]/div/div[3]/div[2]/span')  # 二次确认

    def add_class(self, class_name, teacher_name):
        """增加课时"""
        self.add_class_bt.click()
        self.class_name_loc = class_name
        self.teacher_loc = teacher_name
        today = datetime.datetime.now()
        offset = datetime.timedelta(hours=0.5)  # 当前时间+半小时
        start_time = (today + offset).strftime('%Y-%m-%d %H:%M')
        self.start_time_loc = start_time
        self.save_class_bt.click()

    def get_lesson_name(self):
        """获取课时名称"""
        return str(self.lesson_name_loc.text)

    def get_teacher(self):
        """获取老师名字"""
        return str(self.teacher_name_loc.text)

    def modif_name(self, modif_class_name):
        """修改课时名字"""
        self.modif_bt.click()
        self.modif_class_loc = modif_class_name
        self.save_class1_bt.click()

    def remove_class(self):
        """删除课时"""
        self.remove_bt.click()
        self.remove1_bt.click()