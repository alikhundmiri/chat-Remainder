import webbrowser
import time
from selenium import webdriver

driver = webdriver.Chrome()

total_break = 1
break_count = 1
print ('initiating program : Break Time')
time.sleep(2)
print ('Program started at : ' + time.ctime())
while (break_count <= total_break):
    time.sleep(1*60*60)
    print('log ' + str(break_count) + ', break '+ str(break_count) + ' at :' + time.ctime())
    webbrowser.open("https://web.whatsapp.com")
    driver.get("https://web.whatsapp.com")
    break_count = break_count + 1
print ('Program ended at : ' + time.ctime())    

    
