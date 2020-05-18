'''
@Time  : 2020/5/15 14:58
@Author: fengzhj
@doc   : 教师管理页面
'''

from poium import Page, PageElement

class Teacher_mangerpage(Page):
    manger_title_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[1]/strong')  # 老师管理页面title，用于断言
    add_teacher_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/span')  # 添加老师
    add_teacher_title_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/span')  # 头像标题，用于断言
    add_teacher_all_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/span')  # 批量添加老师
    find_phone_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div/input')  # 手机号查询
    find_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/input')  # 姓名查询
    phone_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody/tr/td[2]')  # 结果中的电话
    name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody/tr/td[1]')  # 结果中的姓名
    find_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/span')  # 查询
    edit_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/div/span[1]')
    del_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/div/span[2]')

    # def teacher_manger(self):
    #     """进入老师管理页面，或者用机构管理员账号登录直接跳转"""
    #     self.get("https://webapp.leke.cn/lt-web/index.html#/management/teacher")
    def get_tcmangertitle(self):
        """老师管理页面title"""
        print(str(self.manger_title_loc.text))
        return str(self.manger_title_loc.text)

    def add_teacher(self):
        """增加老师"""
        self.add_teacher().click()

    def find_teacher_phone(self,phone):
        """通过号码查找老师"""
        self.find_phone_loc = phone
        self.find_bt.click()

    def get_phone(self):
        """获取号码"""
        return str(self.phone_loc.text)

    def find_teacher_name(self,name):
        """通过姓名查找老师"""
        self.find_name_loc = name
        self.find_bt.click()

    def get_name(self):
        """获取姓名"""
        return str(self.name_loc.text)

    def edit_TC(self):
        """编辑老师信息:查询到老师后操作"""
        self.edit_bt.click()
        pass
        return

    def del_TC(self):
        """删除老师信息：查询到老师后操作"""
        self.del_bt.click()