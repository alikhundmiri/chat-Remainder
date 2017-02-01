#Whatsapp Automator

ONLY FOR PERSONAL PURPOSE

#How it works
1. Fill the text files in directory with your relatives, friends and collegues in the respective directory
2. Fill in the custom text you want to send them. Keep in mind, these will be shuffled and a random text will be sent to one of the people in contacts list
3. in the Script Write your name in the string value given. (on the line 11, i.e. Eleven)
4. Change the salutation text in the line below to what you like. (on the line 13, i.e. Thirteen)

#Installation

you will need the following:
[python 3](https://www.python.org/ftp/python/3.6.0/python-3.6.0-macosx10.6.pkg)
Selenium        'pip install Selenium'
[Selenium Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

If you dont have Chrome Driver installed check out this [video for Mac.](https://www.youtube.com/watch?v=XFVXaC41Xac)

for windows:
1. Download the suitable Chrome driver from [here.](https://sites.google.com/a/chromium.org/chromedriver/downloads)
2. Extract the file and keep it in directory(folder) of your desire, usually in c drive.
3. in the script, Add the following line 
       'chrome_path = r"<YOUR DIRECTORY HERE>"'
4. for more information check out this [video.](https://www.youtube.com/watch?v=bhYulVzYRng)


The necessary dependencies are in the requirements.txt file so just run this before running the actual code to get them installed

''pip install -r requirements.txt''
