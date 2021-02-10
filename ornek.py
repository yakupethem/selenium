from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import base64
import json

username="kazimhas96"
password="hXbtvxUNVOs"

class Fintech:
    def __init__(self, username,password):
        self.browser=webdriver.Chrome()
        #self.browser=webdriver.Firefox()
        self.username=username
        self.password=password
        self.list=[]
    
    def signin(self):
        self.browser.get("https://www.itemsatis.com/")
        time.sleep(3)

        self.browser.find_element_by_xpath("//*[@id='CekilisModal']/div/div/div[1]/button").click()
        time.sleep(3)        

        self.browser.find_element_by_xpath("/html/body/header/nav[2]/div/div[3]/ul/li").click()
        time.sleep(3)           

                 
        
        self.browser.find_element_by_css_selector("div[role=dialog] form").find_element_by_name('UserName').send_keys(self.username)
        a=self.browser.find_element_by_css_selector("div[role=dialog] form").find_element_by_name('Password')
        time.sleep(2)
        a.send_keys(self.password)
        a.send_keys(Keys.ENTER)
        time.sleep(2)        
        favoriteItem=self.browser.find_element_by_xpath("/html/body/section[3]/div/div/div/div[1]/ul/li[4]/span")
        favoriteItem.click()
    

            
    def bilgiler(self):
       
        favori=self.browser.find_element_by_id("favori-ilanlar").find_elements_by_class_name("AdvertBox-1")
        time.sleep(1)
        
        for eleman in favori:
            
            fiyat=eleman.find_element_by_class_name("AdvertBox-Price").text
            link=eleman.find_element_by_tag_name("a").get_attribute("href")
            src=eleman.find_element_by_class_name("AdvertBox-Image-1").get_attribute("src")

            byt=base64.urlsafe_b64encode(src.encode("utf-8"))
            base=str(byt,"utf-8")
            
            self.list.append({"fiyat":fiyat,
                               "resim_link" :src,
                               "link":link,
                               "resim_base64":str(base)})

            with  open("ornek.json","w") as f :
                json.dump(self.list,f,indent=4) 

fintech=Fintech(username=username,password=password)
fintech.signin()
fintech.bilgiler()
          

    