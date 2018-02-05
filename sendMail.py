#!/usr/bin/python3

"""
@file: sendMail.py
@brief: 使用Python发送电子邮件
@author: feihu1996.cn
@date: 18-01-24
@version: 1.0
"""

import smtplib,sys,logging
from email.mime.text import MIMEText
from email.header import Header

logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s")

class Sendmail:
	def __init__(self, mailHost, mailUser, mailPassword, sender, receiverList, msgPlain, subject, mailType):
		# smtp服务器
		self.mailHost = mailHost
		# 用户名
		self.mailUser = mailUser
		# 密码
		self.mailPassword = mailPassword
		# 发送方
		self.sender = sender
		# 接收方列表
		self.receiverList = receiverList
		# 邮件正文
		self.msgPlain = msgPlain
		# 邮件主题
		self.subject = subject
		# 邮件MIME类型
		self.mailType = mailType
	def sendMail(self):
		# 邮件正文
		message = MIMEText(self.msgPlain, self.mailType, 'utf-8')
		message['From'] = Header(self.mailUser)
		message['To'] = Header(",".join(self.receiverList))
		message['Subject'] = Header(self.subject, 'utf-8')

		try:
			smtpObj = smtplib.SMTP()
			smtpObj.connect(self.mailHost, 25)
			smtpObj.login(self.mailUser,self.mailPassword)
			smtpObj.sendmail(self.sender, self.receiverList, message.as_string())
			logging.debug("邮件发送成功")
		except smtplib.SMTPException as e:
			logging.debug(e)

if __name__ == "__main__":
	# Sendmail(mailHost, mailUser, mailPassword, sender, receiverList, msgPlain, subject, mailType).sendMail()

