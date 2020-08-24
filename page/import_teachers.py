from poium import Page, PageElement, PageWait
import time
class Importtcspage(Page):
    file_bt = PageElement(xpath = '//span[text()="上传文件"]')  #上传文件
    submit_bt = PageElement(xpath = '(//span[text()="开始导入"])')      #导入按钮
    back_bt = PageElement(link_text = '返回列表')        #导入成功返回列表按钮
    success = PageElement(xpath = '(//td[@class="ant-table-row-cell-break-word"])[2]')

    def import_tcs(self):
        self.file_bt = r"E:\pic\UItest.xls"
        time.sleep(5)
        PageWait(self.submit_bt)
        self.submit_bt.click()

    def get_im_status(self):
        return str(self.success.text)


