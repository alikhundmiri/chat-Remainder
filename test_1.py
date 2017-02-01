from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

global driver
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")
time.sleep(20)
#find search box
web_obj = driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')
#enter the search name
web_obj.send_keys("mummyy")
#get the correct chat from query list
time.sleep(3)
web_obj.send_keys(Keys.RETURN)
print("Enter on chat")
chat_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
print("Writing Message")
time.sleep(3)
chat_obj.send_keys("hi \n as salamu alaykum\n kaise hai aap?\n sab khariyath?")
print("Message ready")
time.sleep(3)
chat_obj.send_keys(Keys.RETURN)
print("Message sent!")
#chat_obj.click()
