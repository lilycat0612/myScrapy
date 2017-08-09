#coding:utf-8
import os
import unittest
import time
from selenium import webdriver



'richardpenman / home &mdash; Bitbucket'
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

class DownloadBtFiles(unittest.TestCase):
    def setUp(self):
        

        url="http://www.ttmeiju.com/index.php/user/myrss.html"

        self.driver=webdriver.Chrome("./chromedriver") #for Chrome

        self.driver.maximize_window()

        self.driver.get(url)


        

    # def test_store_cookie(self):
        
    #     store_cookie=self.driver.get_cookies()

    #     print(store_cookie)
    #     print(len(store_cookie))


    # def tearDown(self):
        # self.driver.quit()
    
    def test_login(self):

        self.inputs=self.driver.find_elements_by_xpath("//input[@class='input_tx']")
        self.inputs[2].send_keys("lilyca0t612")#input username
        self.inputs[3].send_keys("123!@#qwe")#input password


        self.button=self.driver.find_element_by_xpath("//input[@class='input_search']")
        if True == self.button.is_displayed():
            self.button.click()#click login button
        else: 
            print("Fail to click button")

    
        time.sleep(5)#wait for login successfully

        self.driver.find_element_by_xpath("//span[@class='avatar']").click()#Press to transfer to my rss website

        time.sleep(5)

        bt_files=self.driver.find_elements_by_css_selector("a[href*='torrent'][title*='BT']")

        file_count=0
        
        for file in bt_files:
          
            file.click()
            time.sleep(3)
            file_count=file_count+1

        if file_count == len(bt_files):#make sure download all files
            print("Finish Download (%s) BT Files at:"%(file_count),time.asctime())
        else:
            print("Download (%s) BT Files at :" %(file_count),time.asctime())


if __name__=='__main__':
    unittest.main()
    
    