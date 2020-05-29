'''
@Time  : 2020/5/25 16:15
@Author: fengzhj
@doc   : 个人中心账户设置
'''

from poium import Page, PageElement
import time

class Info_page(Page):

    info_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/p[1]')  # 个人资料title
    edit_bt = PageElement(name='editBtn')  # 编辑
    icon_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/span/i')  # 头像
    nick_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/p[2]/input')  # 昵称输入框
    save_bt = PageElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div[3]/button[2]')  # 保存
    nick_title_loc = PageElement(xpath='//*[@id="root"]/div/div[1]/div/div[2]/div[4]/p')  # 菜单栏头像

    def get_title(self):
        """获取个人中心title"""
        return str(self.info_loc.text)

    def modef_nick(self, nick):
        """修改昵称"""
        self.edit_bt.click()
        self.nick_loc.clear()
        self.nick_loc = nick
        time.sleep(1)
        self.save_bt.click()

    def get_nick(self):
        """获取菜单栏昵称"""
        return str(self.nick_title_loc.text)