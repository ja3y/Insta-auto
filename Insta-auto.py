import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#hashtag= input("[+] Please Enter a Trending hashtag: ")
#username = input("[+] Please Enter a User To Follow: ")
driver = webdriver.Chrome("/home/whoami/Documents/chrome_webdriver/chromedriver")
def login():

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    userid=driver.find_elements_by_css_selector('form input')[0].send_keys("Username")
    passid=driver.find_elements_by_css_selector('form input')[1].send_keys("password")

    login= driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
    time.sleep(3)
    #searches for hashtag

    #get_host = driver.get("https://www.instagram.com/explore")

    #driver.get("https://www.instagram.com/")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class = 'aOOlW   HoLwm ']").click()
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.END)
    for post in range(3):
        body.send_keys(Keys.END)
        time.sleep(1)
        body.send_keys(Keys.HOME)
        time.sleep(1)
        like_button =driver.find_element_by_xpath("//button[@class = 'dCJp8 afkep _0mzm-']").click()
    for but in range(30):


        like_button = driver.find_element_by_xpath("//button/span[contains(@class, 'glyphsSpriteHeart__outline__24__grey_9 u-__7')]").click()
        time.sleep(2)
        print ("No of Posts liked: ", but)
    



login()

