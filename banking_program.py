#app startup
import os
import time

os.system('clear')

START=os.getcwd()
START+="/source"
os.chdir(START)
execfile("title.py")

time.sleep(10)

#define current path
PATH=os.getcwd()
#add bank to path
PATH+="/bank"

#define FILE_EXISTS variable as a boolean depending if the bank folder exists
FILES_EXISTS=(os.path.isdir(PATH))

if FILES_EXISTS==False:
    print "I see it is the first time you are using this program"
    print "We will start by creating an account for you!"
    os.mkdir(PATH)
    execfile("create_account.py")
    print"A new account as been created for you you are now ready to go"

execfile("menu.py")

