from poium import Page, PageElement
import time
from util.winuploadfile import WinUpLoadFile
from util.MysqlUtil import MysqlUtil

class Joinorgpage(Page):

    """
    url = https://webapp.leke.cn/lt-web/index.html#/join-apply
    机构信息填写
    """
    #上传机构图片
    pic_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div[2]/div/span/div/div[2]/div[1]/span/div/span/div')
    #机构名称输入框
    name_loc = PageElement(id_ = 'JoinApply_name')
    #机构简介输入框
    briefIntrod_loc =  PageElement(id_ = 'JoinApply_briefIntrod')
    #机构一句话简介
    shortIntrod_loc = PageElement(id_ = 'JoinApply_shortIntrod')
    #公司名称
    companyName_loc = PageElement(id_ = 'JoinApply_companyName')
    #资质证明
    licensepic_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[3]/div[2]/div/span/div/div[2]/div[1]/span/div/span/div/span')
    #资质证明编码
    licenseCode_loc = PageElement(id_ = 'JoinApply_licenseCode')
    #教育资质证明
    certpic_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[5]/div[2]/div/span/div/div[2]/div[1]/span/div/span/div/span')
    #教育资质编码
    certNum_loc = PageElement(id_ = 'JoinApply_certNum')
    #联系人
    contactName_loc = PageElement(id_ = 'JoinApply_contactName')
    #手机号
    phone_loc = PageElement(id_ = 'JoinApply_phone')
    #邮箱
    email_loc = PageElement(id_ = 'JoinApply_email')
    #协议
    isReadedAgreement_loc = PageElement(id_ = 'JoinApply_isReadedAgreement')
    #提交审核
    submit_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/form/div[3]/div/span')
    #二次确认
    confirm_bt = PageElement(css = 'body > div:nth-child(10) > div > div.ccp-mc-confirm-footer > div.ccp-custom-button.small.primary.ccp-mc-confirm-footer-btn.radius > span')


    def org_apply(self):
        self.get('https://webapp.leke.cn/lt-web/index.html#/join-apply')
        self.pic_bt.click()
        time.sleep(2)
        WinUpLoadFile().winUpLoadFile("C:\\Users\\Administrator\\Pictures\\1.jpg", "打开")
        time.sleep(10)
        self.name_loc = 'UI自动化机构名称'
        self.briefIntrod_loc = 'UI自动化机构的长简介'
        self.shortIntrod_loc = 'UI自动化机构的短简介'
        self.companyName_loc = 'UI自动化公司名称'
        self.licensepic_bt.click()
        WinUpLoadFile().winUpLoadFile("C:\\Users\\Administrator\\Pictures\\2.bmp", "打开")
        self.licenseCode_loc = 'yingyezhizhao20200514'
        self.certpic_bt.click()
        WinUpLoadFile().winUpLoadFile("C:\\Users\\Administrator\\Pictures\\3.bmp", "打开")
        self.certNum = 'jiaoyuzizhi20200514'
        self.contactName_loc = 'UI自动化'
        self.phone_loc = '15905140001'
        self.email_loc = '15905140001@cnstrong.cn'
        self.isReadedAgreement_loc.click()
        self.submit_bt.click()
        time.sleep(10)
        Joinorgpage(self.driver)
        self.confirm_bt.click()

    def org_pass(self):
        '''
        后台审核通过+角色变化
        :return:
        '''
        db = MysqlUtil()
        sql = ''
        userid = db.fetchone('select userid from lt_user where isDeleted = 0 and phone = 15905140001;')
        orgid = db.fetchone("select id from lt_org where isDeleted = 0 and name = 'UI自动化机构名称';")
        db.update("UPDATE lt_org set status = 2 where name = 'UI自动化机构名称' and isDeleted = 0;UPDATE lt_user set roleId = 101 where isDeleted = 0 and userid = " + userid +  ";")
        db.insert("INSERT INTO lt_org_teacher_mapping(userId, orgId, userName, summary, photo, isDeleted, createdOn, createdBy, modifiedOn, modifiedBy) VALUES (" + userid + ", " + orgid + ", NULL, NULL, NULL, 0, NOW(), 0, NOW(), 888);")
