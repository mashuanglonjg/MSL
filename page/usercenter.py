from poium import Page,PageElement
from page.orgapply import Joinorgpage

class Usercenter_page(Page):


    def org(self):
        '''
        宣传页、机构入驻填写
        '''
        self.get('https://webapp.leke.cn/lt-web/index.html#/join-propaganda')
        self.get('https://webapp.leke.cn/lt-web/index.html#/join-apply')
        return Joinorgpage(self.driver)