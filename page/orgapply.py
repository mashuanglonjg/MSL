from poium import Page, PageElement, PageWait

class Joinorgpage(Page):

    """
    url = https://webapp.leke.cn/lt-web/index.html#/join-apply
    机构信息填写
    """
    #上传机构图片
    pic_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]'
                                 '/div[1]/div[2]/div/span/div/div[2]/div[1]/span/div/span/input')
    #机构名称输入框
    name_loc = PageElement(id_ = 'JoinApply_name')
    #机构简介输入框
    brief_loc =  PageElement(xpath = '//*[@id="JoinApply_briefIntrod"]')
    #机构一句话简介
    short_loc = PageElement(id_ = 'JoinApply_shortIntrod')
    #公司名称
    companyName_loc = PageElement(id_ = 'JoinApply_companyName')
    #资质证明
    licensepic_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[3]/div[2]/div/span/div/div[2]/div[1]/span/div/span/input')
    #资质证明编码
    licenseCode_loc = PageElement(id_ = 'JoinApply_licenseCode')
    #教育资质证明
    certpic_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[5]/div[2]/div/span/div/div[2]/div[1]/span/div/span/input')
    #教育资质编码
    certNum_loc = PageElement(id_ = 'JoinApply_certNum')
    #联系人
    contactName_loc = PageElement(id_ = 'JoinApply_contactName')
    #手机号
    phone_loc = PageElement(id_ = 'JoinApply_phone')
    #邮箱
    email_loc = PageElement(id_ = 'JoinApply_email')
    #协议
    isReadedAgreement_loc = PageElement(xpath = '//*[@id="JoinApply_isReadedAgreement"]')
    #提交审核
    submit_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[3]/div/span')
    #二次确认
    confirm_bt = PageElement(name = 'sureBtn')

    def org_apply(self):
        #self.get('https://webapp.leke.cn/lt-web/index.html#/join-apply')
        self.pic_bt = r"C:\Users\Administrator\Pictures\1.jpg"
        self.name_loc = 'UI自动化机构名称'
        self.brief_loc = 'UI自动化机构的长简介'
        self.short_loc = 'UI自动化机构的短简介'
        self.companyName_loc = 'UI自动化公司名称'
        self.licensepic_bt = r"C:\Users\Administrator\Pictures\2.bmp"
        self.licenseCode_loc = 'yingyezhizhao20200514'
        self.certpic_bt = r"C:\Users\Administrator\Pictures\3.bmp"
        self.certNum_loc = 'jiaoyuzizhi20200514'
        self.contactName_loc = 'UI自动化'
        self.phone_loc = '15905140001'
        self.email_loc = '15905140001@cnstrong.cn'
        self.isReadedAgreement_loc.click()
        self.submit_bt.click()
        PageWait(self.confirm_bt)
        self.confirm_bt.click()

