#!/usr/bin/python3

"""
@file: sendMail.py
@brief: 使用Python发送电子邮件
@author: feihu1996.cn
@date: 18-01-24
@version: 1.0
"""


from email.mime.text import MIMEText
from email.header import Header
import logging, smtplib, traceback


class Sendmail:
    def __init__(self, mailHost, mailUser, mailPassword, sender):
        # smtp服务器
        self.mailHost = mailHost
        # 用户名
        self.mailUser = mailUser
        # 密码
        self.mailPassword = mailPassword
        # 发送方
        self.sender = sender
        logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s")

    
    def sendMail(self, receiverList, msgPlain, subject, mailType):
        # 邮件正文
        message = MIMEText(msgPlain, mailType, 'utf-8')
        message['From'] = Header(self.mailUser)
        message['To'] = Header(",".join(receiverList))
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mailHost, 25)
            smtpObj.login(self.mailUser,self.mailPassword)
            smtpObj.sendmail(self.sender, receiverList, message.as_string())
            logging.debug("邮件发送成功")
        except smtplib.SMTPException as e:
            logging.debug(e)


if __name__ == "__main__":
    # Sendmail(mailHost, mailUser, mailPassword, sender).sendMail(receiverList, msgPlain, subject, mailType)
    pass

