from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import random
import time
import os
import datetime

##############################################################################
#change the salutation here:
custom_salutations = "As Salam Wa Alaykum, "
##############################################################################
#DO NOT CHANGE THE CODE BELOW
your_name = ""
d_ = datetime.datetime.now()
month = d_.strftime("%B")
list_1 = []
fnd_m_list = []
fnd_nm_list = []
greeting_message_family = []
greeting_message_m_friends = []
greeting_message_nm_friends = []
launch_count = 0

def web_driver_load():
    global driver
    print("Launching Chrome")
    driver = webdriver.Chrome()
    print("Chrome Launched!")

def launch_whatsapp():
    print("Opening Whatsapp Web")
    driver.get('https://web.whatsapp.com/')
    #replace this with an iplicit timer
    print("Please Scan you phone to Login Whatsapp web")
    try:
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "side")))
    except:
        raise fail_to_login()

    if element:
        open_info = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/div')
        open_info.click()
        wait(3)
        chate_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div')
        print("Logged In as " + chate_name.text)
        back_to_chats = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/div/header/div/div/span')
        back_to_chats.click()
        return chate_name.text

    else:
        fail_to_login()

def fail_to_login():
    print("Failed to Sign in to Whatsapp Web")
    driver.get('')
    print("Quiting Script")
    exit()

def update_chats():
    here_is_us = os.getcwd()
    os.chdir(here_is_us)

    if len(greeting_message_family) == 0:
        print("Updating the chat templates for Family")
        # update the family chat template list
        file_a = open('chat_templates/chats_1.txt', 'r')
        line_f = file_a.readlines()
        for names_list_1 in line_f:
            if names_list_1 not in greeting_message_family:
                greeting_message_family.append(names_list_1)
        file_a.close()
    else:
        pass

    if len(greeting_message_m_friends) == 0:
        print("Updating the chat templates for Friends_1")
        # update the friends_1 chat template list
        file_m = open('chat_templates/chats_2.txt', 'r')
        line_m = file_m.readlines()
        for fnd_m in line_m:
            if fnd_m not in greeting_message_m_friends:
                greeting_message_m_friends.append(fnd_m)
        file_m.close()
    else:
        pass
    if len(greeting_message_nm_friends) == 0:
        print("Updating the chat templates for Friends_2")
        # update the friends_2 chat template list
        file_nm = open('chat_templates/chats_3.txt', 'r')
        line_nm = file_nm.readlines()
        for fnd_nm in line_nm:
            if fnd_nm not in greeting_message_nm_friends:
                greeting_message_nm_friends.append(fnd_nm)
        file_nm.close()
    else:
        pass

def update_list():
    #if file for month doesnt exist, make one
    if not os.path.isfile(file_name):
        write_txt(file_name, "")
    file_chats = open(file_name,'r')
    fc = file_chats.read()

    file_a = open('List/family.txt', 'r')
    line_f = file_a.readlines()
    for names_list_1 in line_f:
        if names_list_1 not in list_1:
            if names_list_1 not in fc:
                list_1.append(names_list_1)
    file_a.close()

    # update the friends M list
    file_m = open('List/friends_m.txt', 'r')
    line_m = file_m.readlines()
    for fnd_m in line_m:
        if fnd_m not in fnd_m_list:
            if fnd_m not in fc:
                fnd_m_list.append(fnd_m)
    file_m.close()

    # Update the friends NM list
    file_nm = open('List/friends_nm.txt', 'r')
    line_nm = file_nm.readlines()
    for fnd_nm in line_nm:
        if fnd_nm not in fnd_nm_list:
            if fnd_nm not in fc:
                fnd_nm_list.append(fnd_nm)
    file_nm.close()
    file_chats.close()

def exhausted_the_list():
    print("Hey! "+your_name+"!, You have Exhausted the chat list for the month of " + d_.strftime("%B")+".")
    print("Closing the Script...")
    exit()

def generate_abc(length):
    numa = 0
    a__ = [numa, ]
    numb = 1
    b__ = [numb, ]
    numc = 2
    c__ = [numc, ]
    for i in range(0, length):
        numa = numa + 3
        a__.append(numa)
        numb = numb + 3
        b__.append(numb)
        numc = numc + 3
        c__.append(numc)
    return [a__, b__, c__]

def start_timer():
    f_len = len(list_1)
    m_list = len(fnd_m_list)
    nm_list = len(fnd_nm_list)
    print('You Have a total of '+str(f_len + m_list + nm_list)+' people to chat with!.')
    print('Family  : ' +str(f_len))
    print('Friends : ' +str(m_list + nm_list))
    if f_len+m_list+nm_list==0:
        exhausted_the_list()
    else:
        pass
    chats_today = input("How many Chats you plan today?\n recommended Chats: 6 \n maximum value: "+str(f_len + m_list + nm_list)+ "\n >> ")
    if type(chats_today) == int:
        chats_today = input("PLEASE ENTER A VALID INT VALUE\n recommended Chats: 6 \n maximum value: " + str(f_len + m_list + nm_list) + "\n >> ")
        if type(chats_today) == int:
            print("SORRY YOU HAVE TO START THE PROGRAM AGAIN!")
            exit()
        else:
            pass
    else:
        pass
    print("Starting the Timer for 30 minute @ " + time.ctime())
    a__ = []
    b__ = []
    c__ = []
    token = 0
    for i in range(0, int(chats_today)):
        person_bg = '9'
        print("\n\tInitiating Selection " + str(i+1) + "\n" )
        if i == 0:
            #get the length of largest array and send it to generate_abc
            if (f_len > m_list) and (f_len > nm_list):
                largest = f_len
            elif (m_list > f_len) and (m_list > nm_list):
                largest = m_list
            else:
                largest = nm_list
            a__, b__, c__ = generate_abc(largest)
            a_ = random.randint(3, 15)
            time.sleep(a_)
            b_ = random.randint(7, 27)
            time.sleep(b_)

        else:
            # Wait between two consequtive chats initiations
            wait(3 * 60)#10 minutes and random seconds
            c_ = random.randint(7, 217)
            time.sleep(c_)
            d_ = random.randint(4, 156)
            time.sleep(d_)

        if i in a__:
            if len(list_1) != 0:
                person_bg = "family"
                print("\t\tChat with: Family")
            else:
                pass
        elif i in b__:
            if len(fnd_m_list) != 0:
                person_bg = "fnd_m"
                print("\t\tChat with: Friend")
            else:
                pass
        elif i in c__:
            if len(fnd_nm_list) != 0:
                person_bg = "fnd_nm"
                print("\t\tChat with: Friend")
            else:
                pass
        if person_bg is '9':
            if token < 6:
                token = token +1
                print(str(token))
                continue
            else:
                exhausted_the_list()
        else:
            name = get_chatlist(person_bg)
            if name is 'ocxrttty':
                continue
            else:
                chat_(name, person_bg)

def get_chatlist(what):
    name = get_a_name(what, file_name)
    if name == None:
        get_chatlist(what)
    else:
        return name

def get_a_name(what, location):
    new_name = "ocxrttty"
    if what == 'family':
        if len(list_1) > 0:
            random.shuffle(list_1)
            new_name = list_1.pop()
        elif len(list_1) == 0:
            print("You have Talked to all the People in family_list")
            new_name = "ocxrttty"
    elif what == 'fnd_m':
        if len(fnd_m_list) > 0:
            random.shuffle(fnd_m_list)
            new_name = fnd_m_list.pop()
        elif len(fnd_m_list) == 0:
            print("You have Talked to all the People in m_list")
            new_name = "ocxrttty"
    elif what == 'fnd_nm':
        if len(fnd_nm_list) > 0:
            random.shuffle(fnd_nm_list)
            new_name = fnd_nm_list.pop()
        elif len(fnd_nm_list) == 0:
            print("You have Talked to all the People in nm_list")
            new_name = "ocxrttty"
    new_name = new_name.replace('\n','')
    #if name is in archives, send to check_new_name(what, where)
    if check_new_name(new_name, location):
        #this person was already talked to, choose another
        get_a_name(what, location)
    else:
        if new_name is "ocxrttty":
            pass
        else:
            Write_this =" @ " + time.ctime() + " with " + new_name
            write_txt(location, Write_this)
        return new_name

def check_new_name(check_this, in_here):
    archives = open(in_here, 'r')
    check = archives.read()
    archives.close()
    if check_this is "ocxrttty":
        return False
    else:
        if check_this in check:
            return True
        else:
            return False

def chat_(chat_name, chat_bg):

    #find the search box
    web_obj = driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')

    # enter the search name
    web_obj.send_keys(chat_name)

    #replace this with explicit timer
    time.sleep(3)

    web_obj.send_keys(Keys.RETURN)
    print("\t\t\tWe are in the chat now, with : " + chat_name)

    #Search for the Message text box
    chat_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")

    time.sleep(3)

    #Get the text to write
    text = get_chat_message(chat_bg, chat_name)

    #Write the message in text box
    chat_obj.send_keys(text)
    print("\t\t\tMessage ready: \n" + text)

    time.sleep(3)

    #hit enter
    chat_obj.send_keys(Keys.RETURN)
    print("\t\t\tMessage sent!")

def get_chat_message(background , c_name):
    g = random.randint(0, 8)
    if background is "family":
        message = custom_salutations + c_name +"!. \n"+greeting_message_family[g]
    elif background is 'fnd_m':
        message = custom_salutations + c_name +"!!?. :) \n"+greeting_message_m_friends[g]
    elif background is 'fnd_nm':
        message = c_name +"!... "+greeting_message_nm_friends[g]
    else:
        message = "Hi "+c_name+"!, how's it going? all good?"
    return message

def write_txt(path, data):
    f = open(path, 'a')
    f.write(data + "\n")
    f.close()


def wait(web_opening_time=10):
    time.sleep(web_opening_time)

if __name__ == "__main__":
    print("Launching Script...")
    driver = None
    web_driver_load()
    your_name = launch_whatsapp()
    your_name_ = your_name.replace(" ", "_")
    file_name = "Archive/" + your_name_ + "_chat_list_" + month + ".txt"
    update_chats()
    update_list()
    start_timer()

#   open webDriver
