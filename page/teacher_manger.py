'''
@Time  : 2020/5/15 14:58
@Author: fengzhj
@doc   : 教师管理页面
'''

from poium import Page, PageElement

class Teacher_manger_page(Page):
    manger_title_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[1]/strong')  # 老师管理页面title，用于断言

    add_teacher_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/span')  # 添加老师
    add_teacher_title_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/span')  # 头像标题，用于断言
    add_teacher_all_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/span')  # 批量添加老师
    find_phone_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div/input')  # 手机号查询
    find_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/input')  # 姓名查询
    find_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/span')  # 查询




    def teacher_manger(self):
        """进入老师管理页面，或者用机构管理员账号登录直接跳转"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/management/teacher")

    def add_teacher(self):
        """增加老师"""
        self.add_teacher().click()

    def find_teacher_phone(self):
        """通过号码朝招老师"""
