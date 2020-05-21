'''
@Time  : 2020/4/28 19:30
@Author: fengzhj
@doc   : 
'''


from selenium import webdriver
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

def get_pic():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.24.123:8080/view/LT_college/job/LT_college/allure/')
    driver.find_element_by_name('j_username').send_keys('AI')
    driver.find_element_by_name('j_password').send_keys('123456')
    driver.find_element_by_name('Submit').click()
    time.sleep(3)
    pic_name = datetime.datetime.now().strftime('%Y-%m-%d')
    pic_path = 'C:\\Users\\Administrator\\.jenkins\\workspace\\LT_college\\emals-reports\\'+str(pic_name)+'.png'
    #pic_path = '/emals-reports/'+str(pic_name)+'.png'
    driver.save_screenshot(pic_path)
    return pic_path

def send_emails():
    mail_host = "smtp.cnstrong.cn"  # 设smtp置服务器
    mail_user = "fengzhongjie@cnstrong.cn"  # 发送邮箱
    mail_pass = ""  # 授权码
    sender = 'fengzhongjie@cnstrong.cn'
    receiver = ['fengzhongjie@cnstrong.cn', 'guojianxiu@cnstrong.cn']

    # 以html格式构建邮件内容
    send_str = '<html><body>'
    send_str += '<h2>点击图片查看报告详情  用户名：AI，密码：123456</h2>'
    send_str += '<center>测试报告预览</center>'
    send_str += '<a href="http://192.168.24.123:8080/view/cnstrong/job/LT_college/allure/">'
    # html中以<img>标签添加图片，align和width可以调整对齐方式及图片的宽度
    send_str += '<img src="cid:image1" alt="image1" align="center" width=100% >'
    send_str += '</body></html>'
    # 构建message
    msg = MIMEMultipart()

    # 邮件主题
    # title = '乐桃学院UI自动化测试报告'

    msg.add_header("Subject", '乐桃学院UI自动化测试报告')  # 邮件主题
    msg.add_header('from', '测试')  # 设置发送人
    msg.add_header('to', 'AI乐学')  # 设置接收人


    # 添加邮件内容
    content = MIMEText(send_str, _subtype='html', _charset='utf8')
    msg.attach(content)

    # 添加图像对象
    # pic_path = 'C:\\Users\\Administrator\\.jenkins\\workspace\\LT_college\\emals-reports\\2020-04-28.png'
    pic_path = get_pic()
    img1 = MIMEImage(open(pic_path, 'rb').read(), _subtype='octet-stream')
    img1.add_header('Content-ID', 'image1')
    msg.attach(img1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")


if __name__ == '__main__':
    send_emails()
'''
receiver = "guojianxiu@cnstrong.cn"
body = '报告地址：http://192.168.24.123:8080/view/cnstrong/job/LT_college/allure/ \n 用户名：AI，密码：123456'

title = '乐桃学院UI自动化测试报告'
emails.send_email(receiver, title, body)
'''
