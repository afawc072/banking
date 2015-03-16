import os
import commands
import time

os.system('clear')

PATH1=os.getcwd()
PATH=os.getcwd()
#add bank to path
PATH+="/bank/"
os.chdir(PATH)
print"Of what account do you want to see the balance?:"
print ""
ls = commands.getoutput("ls") 
print ls

ACCOUNT=raw_input()

FILE_EXISTS=(os.path.isdir(PATH+ACCOUNT))

if FILE_EXISTS==True:

    BALANCE=PATH+ACCOUNT
    BALANCE += "/balance.txt"
    
    FLAG=False
    f = open(BALANCE,"r") #opens file with name of "test.txt"
    print "Your ",ACCOUNT," contains:"
    print(f.read())
    print"To exit type 'menu'"
    
    while FLAG==False:
	exit=raw_input()
	if exit=="menu":
		FLAG=True
    
os.chdir(PATH1)

