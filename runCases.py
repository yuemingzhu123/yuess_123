import unittest
import HTMLTestRunner
#上一级目录 make 目录，就不红了
from mytestcases import tryBaidu
from mytestcases import tryTestfan
import HTMLTestRunner
#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
#--------------------
mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(tryBaidu.Baidu))
mysuite.addTest(unittest.makeSuite(tryTestfan.Testfan))

filename = 'Casesreport.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='测试报告',
    description='用例执行情况：')
runner.run(mysuite)
######

# 只需要改这些即可，开始
smtpserver = 'smtp.163.com'
username = 'yuess011@163.com'
password = 'yue123'     # 设置客户端授权码 的 密码
sender = 'yuess011@163.com'
# 收件人为多个收件人
receiver = ['yuess011@163.com']
subject = 'Python email test'
mailbody = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.testfan.cn"
# attachfile = "smail.py"
attachfile = filename
# 只需要改这些即可，结束


msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'yuess <yuess@163.com>'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)


# 构造文字内容

text_plain = MIMEText(mailbody, 'plain', 'utf-8')
msg.attach(text_plain)


# 构造附件
sendfile = open(attachfile, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 附件可以重命名成aaa.txt，最好用原来文件名
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=attachfile)
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

