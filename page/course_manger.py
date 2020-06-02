'''
@Time  : 2020/5/27 14:00
@Author: fengzhj
@doc   : 课程管理页面
'''

from poium import Page, PageSelect, PageElement
import time
from page.lesson_name_list import Name_list_page

class Coursemanger_page(Page, PageSelect):

    search_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/span')  # 查找按钮
    search_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/input')  # 搜索课程名字
    search_type_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]')  # 搜索类型
    search_type1_loc = PageElement(xpath='/html/body/div[4]/div/div/div/ul/li[2]')
    search_status_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[3]/div/div/div/div')  # 搜索状态

    course_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div/div'
                                        '/div/table/tbody/tr[1]/td[1]/div/div[2]/p[1]')  # 搜索结果中的课程名字
    course_no_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div'
                                           '/div/div/div/div/div[2]/div/p')  # 没有搜索结果的文案
    course_type_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/'
                                        'div/div/div/table/tbody/tr[1]/td[4]')  # 搜索结果中的课程类型
    course_status_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/'
                                         'div/div/div/div/table/tbody/tr/td[5]')  # 搜索结果中的课程状态
    course_money_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div'
                                         '/div/div/table/tbody/tr/td[1]/div/div[2]/p[2]')  # 搜索结果中的课程价格
    create_lesson_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div'
                                         '/table/tbody/tr/td[6]/div/span[1]')  # 排课
    stu_name_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div/div/div/table'
                                    '/tbody/tr/td[6]/div/span[1]')  # 上课名单
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
    del1_bt = PageElement(name='shanchu-ok')  # 二次确认

    def search_course(self, course_name):
        """查找已发布的直播课"""
        self.search_name_loc = course_name
        time.sleep(1)
        self.search_bt.click()

    def get_course_name(self):
        """获取课程名字"""
        return str(self.course_name_loc.text)

    def get_course_money(self):
        """获取课程总价"""
        return str(self.course_money_loc.text)

    def get_course_type(self):
        """获取课程类型"""
        return str(self.course_type_loc.text)

    def del_course(self):
        """删除直播课"""
        self.del_bt.click()
        self.del1_bt.click()


    def name_list(self):
        """上课名单"""
        self.stu_name_bt.click()
        return Name_list_page(self.driver)




