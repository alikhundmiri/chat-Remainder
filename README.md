# Whatsapp Automator

ONLY FOR EDUCATIONAL/PERSONAL PURPOSE.

DO NOT use it for advertisement purpose!, your Whatsapp Account WILL BE BLOCKED.

## new detailed Walkthrough
Check out the new walkthrough i wrote for this here http://www.alikhundmiri.com/blog/whatsapp-automator-a-guide-for-abecedarian-program or click [here][1]




# How it works
## what you have to do:
1. Fill the text files in directory(List) with your relatives, friends and collegues in the respective directory
2. Fill in the custom text you want to send them. Keep in mind, these will be shuffled and a random text will be sent to one of the people in contacts list
3. Change the salutation text in the line below to what you like. (on the line 13, i.e. Thirteen)
4. In your whatsapp make sure you have entered your name in the "Your Name"

# What it does NOT
1. it doesnt reply to messages to you recieve.
2. it(*script*) doesnt read your conversations and send to 3rd party. :+1:
3. 

# What it does
1. Starts the conversations with the people in the list
2. *thats it*

# How do you work it?
1. write the name of people you want to be in constant touch with.
2. write the custom texts.
3. start the program in command line by `python3 whatsapp_automater.py`.
4. let it read the names and texts.
5. feed in the number of people you want to chat today.
now it will send an *initiative message* to random people from the list*s*

Message Pattern:

1. People in `List/family.txt` will get messages from `chat_templates/chats_1.txt` with Salutation
2. People in `List/friend_n.txt` will get messages from `chat_templates/chats_2.txt` with Salutation
3. People in `List/friends_nm.txt` will get messages from `chat_templates/chats_3.txt` without Saluation


# Installation

you will need the following:
## Preinstalls:
[python 3](https://www.python.org/ftp/python/3.6.0/python-3.6.0-macosx10.6.pkg)
Selenium
[Selenium Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## for Mac and Linux:
If you dont have Chrome Driver installed 
Check out this [video for Mac.](https://www.youtube.com/watch?v=XFVXaC41Xac)

## for windows:
If you dont have Chrome Driver installed 
Check out this [video.](https://www.youtube.com/watch?v=bhYulVzYRng)

## dependencies:
The necessary dependencies are in the requirements.txt file so just run this before running the actual code to get them installed
```
pip install -r requirements.txt
```

 [1]:http://www.alikhundmiri.com/blog/whatsapp-automator-a-guide-for-abecedarian-program
