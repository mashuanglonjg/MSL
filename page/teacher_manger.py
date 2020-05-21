'''
@Time  : 2020/5/15 14:58
@Author: fengzhj
@doc   : 教师管理页面
'''

from poium import Page, PageElement
import time

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
    edit_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/div/span[1]')  # 编辑
    del_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/div/span[2]')  # 删除
    del1_bt = PageElement(id_='sureBtn')  # 二次确认
    tc_name_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/input')  # 编辑中的老师名字
    name_save_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/span')  # 保存
    name_save1_bt = PageElement(name='sureBtn')  # 二次确认
    find_date_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[4]/div[1]/div/div/div/div/div/div[2]/div/p')  # 暂无数据

    # def teacher_manger(self):
    #     """进入老师管理页面，或者用机构管理员账号登录直接跳转"""
    #     self.get("https://webapp.leke.cn/lt-web/index.html#/management/teacher")
    def get_tcmangertitle(self):
        """老师管理页面title"""
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

    def edit_TC(self,tc_name):
        """编辑老师信息（编辑姓名）:查询到老师后操作"""
        self.edit_bt.click()
        self.tc_name_loc.clear()
        self.tc_name_loc = tc_name
        self.name_save_bt.click()
        time.sleep(2)
        self.name_save1_bt.click()


    def del_TC(self,name):
        """删除老师信息：查询到老师后操作"""
        self.find_teacher_name(name)
        time.sleep(2)
        self.del_bt.click()
        time.sleep(2)
        self.del1_bt.click()

    def find_date(self):
        """暂无数据的文案"""
        return str(self.find_date_loc.text)