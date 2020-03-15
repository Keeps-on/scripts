# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# https://blog.csdn.net/weixin_44755148/article/details/92623759

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

# msg_to = ['1299793997@qq.com', '564060577@qq.com']

# email_subject = '测试邮件'
# email_content = '这次是最新的一xxxxxxxxxxxx次测试'
# # 构造邮件
# msg = MIMEText(email_content)
# msg["Subject"] = email_subject
# msg['From'] = msg_from
# # msg['To'] = msg_to
# msg['To'] = ','.join(msg_to)
# print(msg['To'].split(','))
# print(','.join(msg_to))
# subject = "邮件标题"  # 主题
# # 创建一个带附件的实例
# msg = MIMEMultipart()
# # 放入邮件主题
# msg['Subject'] = subject
# # 也可以这样传参
# # msg['Subject'] = Header(subject, 'utf-8')
# # 放入发件人
# msg['From'] = msg_from
#
# # 邮件正文内容
# msg.attach(MIMEText('Python 邮件发送测试……', 'plain', 'utf-8'))
#
#
# # 构造文件附件
# # 构造附件1，传送当前目录下的 test.txt 文件
# att1 = MIMEText(open('email_test.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="test.txt"'
# msg.attach(att1)


# try:
#     smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
#     smtp.login(msg_from, passwd)
#     # smtp.sendmail(msg_from, msg_to, msg.as_string())
#     # smtp.sendmail(msg_from, msg['To'].split(','), msg.as_string())
#     smtp.sendmail(msg_from, msg_to, msg.as_string())
#     print('发送成功')
# except Exception as e:
#     print(e)
#     print('发送失败')


"""

# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : _smtplib.py 



import smtplib
from email.mime.text import MIMEText
from email.header import Header
# msg_from = '***@qq.com'  # 发送方邮箱
msg_from = 'lippjobemail@163.com'  # 发送方邮箱
passwd = 'lipanpan0613'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
# msg_to = ['****@qq.com','**@163.com','*****@163.com']  # 收件人邮箱
msg_to = '1299793997@qq.com'  # 收件人邮箱

subject = "邮件标题"  # 主题
content = "邮件内容，我是邮件内容，哈哈哈"
# 生成一个MIMEText对象（还有一些其它参数）
msg = MIMEText(content)
# 放入邮件主题
msg['Subject'] = subject
# 也可以这样传参
# msg['Subject'] = Header(subject, 'utf-8')
# 放入发件人
msg['From'] = msg_from
# 放入收件人
# msg['To'] = '1299793997@qq.com'
# msg['To'] = '发给你的邮件啊'
try:
    # 通过ssl方式发送，服务器地址，端口
    s = smtplib.SMTP_SSL("smtp.163.com", 465)
    # 登录到邮箱
    s.login(msg_from, passwd)
    # 发送邮件：发送方，收件方，要发送的消息
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('成功')
except s.SMTPException as e:
    print(e)
finally:
    s.quit()



"""
# https://www.jianshu.com/p/37208d18eb64
# https://blog.csdn.net/weixin_44755148/article/details/92623759 发送到多人
# 发送附件
