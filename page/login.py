'''
@Time    : 2020/04/27 16:03
@Author  : fzj
@Desc    : 登录页
'''
from poium import Page, PageElement

class Loginpage(Page):
    sms_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/span')  # 切换手机号输入
    pw_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/span')  # 切换密码输入
    loginname_loc = PageElement(name='login-username')
    password_loc = PageElement(name='login-password')
    login_loc = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]')
    findpwd_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[4]/span')  # 找回密码
    findpwd_title = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/strong')  # 找回密码标题
    black_bt = PageElement(xpath='/html/body/div[1]/div/div[2]/div/div/div[1]/span')  # 返回


    def findpwd(self):
        """点击找回密码"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/login")
        self.pw_bt.click()
        self.findpwd_bt.click()

    def get_findpwd_title(self):
        """获取找回密码页面的文案"""
        return str(self.findpwd_title.text)

    def black(self):
        self.black_bt.click()



    def login(self,loginname,password):
        """登录"""
        self.get("https://webapp.leke.cn/lt-web/index.html#/login")
        self.pw_bt.click()
        self.loginname_loc = loginname
        self.password_loc = password
        self.login_loc.click()

