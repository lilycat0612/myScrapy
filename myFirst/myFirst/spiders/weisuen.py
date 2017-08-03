
#coding=utf-8
#-*-coding:utf-8-*-
import scrapy
from myFirst.items import MyfirstItem
import os

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
        
