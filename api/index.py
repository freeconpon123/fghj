from http.server import BaseHTTPRequestHandler
import hashlib
import random
import requests
import time
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class handler(BaseHTTPRequestHandler):
    def sendemail(self):
      # 设置发件人和收件人
      sender = 'tangsongbj@gmail.com'
      recipient = 'g16661666@163.com'
      # 创建电子邮件消息
      msg = MIMEMultipart()
      msg['From'] = sender
      msg['To'] = recipient
      msg['Subject'] = 'Test email from Python'
      # 添加正文
      body = 'This is a test email from Python'
      msg.attach(MIMEText(body, 'plain'))
      # 配置 SMTP 服务器
      smtp_server = 'smtp-relay.sendinblue.com'
      smtp_port = 587
      smtp_username = 'tangsongbj@gmail.com'
      smtp_password = '8AbILBNPaSQ7KRx9'
      # 发送电子邮件
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(smtp_username, smtp_password)
          server.sendmail(sender, recipient, msg.as_string())

    def do_GET(self):
        self.sendemail()
        url = 'https://smstome.com/country/france'
        tag_name = 'div'
        class_name = 'numview'
        phone_tag_name = 'a'
        phone_class_name = 'button'

        # 获取电话号码的初始内容
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        phone_content = soup.find(tag_name, {'class': class_name}).find(phone_tag_name, {'class': phone_class_name}).get_text()
        
        # 持续监控电话号码的变化
        while True:
            
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            new_phone_content = soup.find(tag_name, {'class': class_name}).find(phone_tag_name, {'class': phone_class_name}).get_text()
            if new_phone_content != phone_content:
                self.sendemail()
                phone_content = new_phone_content
            time.sleep(20)  # 每隔60秒进行一次检查
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
