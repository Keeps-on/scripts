# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : _email_file.py
# https://blog.csdn.net/weixin_44755148/article/details/92623759


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发件人信息
msg_from = 'lippjobemail@163.com'
passwd = 'lipanpan0613'

# 收件人信息
msg_to = '1299793997@qq.com'

# 邮件主题
subject = "邮件标题"  # 主题

# 邮件正文内容
text = "带附件的邮件测试"
mail_inside = MIMEText(text, 'plain', 'utf-8')

# 创建一个带附件的实例
msg = MIMEMultipart()
# 放入邮件主题
msg['Subject'] = subject
# 也可以这样传参
# msg['Subject'] = Header(subject, 'utf-8')
# 设置收件人
msg['From'] = msg_from
# 设置发件人
msg['TO'] = msg_to
# 传入邮件正文内容
msg.attach(mail_inside)  # 将文本文件的内容传入

# 构建文件附件
attr1 = MIMEText(open('email_test.txt', 'rb').read(), 'base64', 'utf-8')
attr1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
attr1["Content-Disposition"] = 'attachment; filename="test.txt"'
msg.attach(attr1)

try:
    smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
    smtp.login(msg_from, passwd)
    smtp.sendmail(msg_from, msg_to, msg.as_string())
    # smtp.sendmail(msg_from, msg['To'].split(','), msg.as_string())
    print('发送成功')
except smtp.SMTPException as e:
    print(e)
finally:
    smtp.quit()


