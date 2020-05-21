'''
@Time    : 2020/04/27 16:03
@Author  : fzj
@Desc    : 登录页，根据不同角色返回不同的着陆页
'''
from poium import Page, PageElement
from page.admin_manger import Adminpage
from page.usercenter import Usercenter_page

class Loginpage(Page):
    sms_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/span')  # 切换手机号输入
    pw_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/span')  # 切换密码输入
    loginname_loc = PageElement(name='login-username')
    password_loc = PageElement(name='login-password')
    login_loc = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]')
    findpwd_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[4]/span')  # 找回密码
    findpwd_title = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/strong')  # 找回密码标题
    back_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/span')  # 返回
    service_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[3]/em')  # 服务协议
    service_title = PageElement(xpath='/html/body/div[2]/div/div[1]/strong')  # 服务协议title
    service_text = PageElement(class_name='ccp-custom-modal-body')  # 服务协议文本
    service_quit_bt = PageElement(xpath='/html/body/div[2]/div/div[3]/div/span')  # 我知道了
    title_loc = PageElement(xpath='//*[@id="root"]/div/div[2]/div[1]/ul/li[2]/div/div/span')  # 定位到教务教学断言登录成功


    def findpwd(self):
        """点击找回密码"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/login")
        self.pw_bt.click()
        self.findpwd_bt.click()

    def get_findpwd_title(self):
        """获取找回密码页面的文案"""
        return str(self.findpwd_title.text)

    def back(self):
        """返回"""
        self.back_bt.click()

    def service(self):
        """点击服务协议"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/login")
        self.service_bt.click()

    def get_service_title(self):
        """获取服务协议标题"""
        return str(self.service_title.text)

    def get_service_text(self):
        """获取服务协议文本"""
        return str(self.service_text.text)

    def service_quit(self):
        """点击我知道了"""
        self.service_quit_bt.click()

    def get_title_loc(self):
        """获取机构导航栏文本"""
        return str(self.title_loc.text)

    def admin_login(self, loginname, password):
        """登录"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/login")
        self.pw_bt.click()
        self.loginname_loc = loginname
        self.password_loc = password
        self.login_loc.click()
        return Adminpage(self.driver)

    def user_login(self, loginname, password):
        """登录"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/login")
        self.pw_bt.click()
        self.loginname_loc = loginname
        self.password_loc = password
        self.login_loc.click()
        return Usercenter_page(self.driver)

