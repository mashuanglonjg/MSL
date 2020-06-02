from poium import Page, PageElement, PageWait
import time
class Importtcspage(Page):
    file_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[3]/div/span/input')  #上传文件
    submit_bt = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div')      #导入按钮
    back_bt = PageElement(link_text = '返回列表')        #导入成功返回列表按钮
    success = PageElement(xpath = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/table/tbody/tr/td[2]')

    def import_tcs(self):
        self.file_bt = r"E:\pic\UItest.xls"
        time.sleep(5)
        PageWait(self.submit_bt)
        self.submit_bt.click()

    def get_im_status(self):
        return str(self.success.text)


