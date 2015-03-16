#Main Menu for the application
import os

PATH=os.getcwd()
#add bank to path
PATH+="/bank/"
#os.chdir(PATH)
EXIT_FLAG="quit"
input=""

while input != "quit":
    os.system('clear')
    print"MAIN MENU"
    print""
    print"To exit the program, enter 'quit'!"
    print "Please select the option you would like"
    print ""
    print ""
    print "1 - Add A Transactions To An Account"
    print ""
    print "2 - View The Balance Of An Account"
    print ""
    print "3 - View Recent Transactions Of An Account"
    print ""
    print "4 - Add An Account"
    print ""
    
    
    input=raw_input()

    if input=="1":
        execfile("transactions.py")
    if input=="2":
        execfile("balance.py")
    if input=="3":
        execfile("view_transactions.py")
    if input=="4":
        execfile("create_account.py")
