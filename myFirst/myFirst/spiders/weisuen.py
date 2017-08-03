
#coding=utf-8
#-*-coding:utf-8-*-
import scrapy
from myFirst.items import MyfirstItem
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTPAuthenticationError

#hard code need to changed
username = 'rpi_report_ip@outlook.com'  # Email Address from the email you want to send an email
password = 'ThisIsRobot'  # Password
server = smtplib.SMTP('')
from_addr='rpi_report_ip@outlook.com'

# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg):
    #server = smtplib.SMTP('smtp-mail.outlook.com', '587')
    server = smtplib.SMTP('Smtp.live.com', '25')#hard code need to changed
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

class WeisuenSpider(scrapy.Spider):
    name='weisuen'

    start_urls=("http://ipaddress.com",)
    
    def parse(self,response):
        

        #MyIP=response.xpath("//p[@class='navbar-text navbar-right text-right visible-lg-block']/text()")

        MyIP = ''.join(response.xpath("//p[@class='navbar-text navbar-right text-right visible-lg-block']/text()").extract()).strip()
        
        file_object = open('IP.txt', 'r')
        old_IP = file_object.read()

        if MyIP==old_IP:
            print('The IP does NOT change')
            file_object.close()
            
        else:#if the IP address changed to write it down and send email 
            print('The IP DO change')           
            file_object = open('IP.txt', 'w')
            file_object.write(MyIP)
            file_object.close()
            email_list = [line.strip() for line in open('email.txt')] #for windows #hard code need to changed

            for to_addrs in email_list:
                msg = MIMEMultipart()
                msg['Subject'] = "You IP address has changed" + MyIP
                msg['From'] = from_addr
                msg['To'] = to_addrs


                try:
                    send_mail(username, password, from_addr, to_addrs, msg)
                    print ("Email successfully sent")
                #The sever doesn't accept username and password
                except SMTPAuthenticationError:
                    print ('SMTPAuthenticationError')
                    print ("Email NOT sent")
