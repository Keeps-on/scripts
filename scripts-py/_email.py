# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : _email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



##################################################
#              单人发送邮件
##################################################

# 发件人信息
msg_from = 'lippjobemail@163.com'
passwd = 'lipanpan0613'

# 收件人信息
msg_to = '1299793997@qq.com'

# 邮件内容
email_content = "单人发送邮件测试"
email_subject = "邮件主题测试"
msg = MIMEText(email_content)
msg["Subject"] = email_subject
msg['From'] = msg_from
msg['To'] = msg_to

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

