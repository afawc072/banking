import os
import commands
import datetime

os.system('clear')

PATH1=os.getcwd()
PATH=os.getcwd()
#add bank to path
PATH+="/bank/"
os.chdir(PATH)
print"In what account do you want to add a transaction?(Type the name):"
print ""
ls = commands.getoutput("ls") 
print ls

ACCOUNT=raw_input()

FILE_EXISTS=(os.path.isdir(PATH+ACCOUNT))

if FILE_EXISTS==True:
    TYPEFLAG=False
    while TYPEFLAG==False:
        print"Is it a retreat or a spending(type 'withdrawl' or 'deposit')"
        TYPE=raw_input()
        if TYPE=="deposit" or TYPE=="withdrawl":
            TYPEFLAG=True
    print"What is the amount"
    AMOUNT=raw_input()
    AMOUNT=float(AMOUNT)
    print"What is the reason for this retreat (optionnal)"
    REASON=raw_input()
    
    TODAY = str(datetime.date.today())
        
        
    print "Date: ",TODAY
    print "Type: ",TYPE
    print "Amount:",AMOUNT
    print "Reason: ",REASON
    print ""
    print "Is this information exact?('yes' or 'no'):"
    FLAG=raw_input()
    if FLAG=="yes":
        

        TRANSACTIONS=PATH+ACCOUNT
        TRANSACTIONS += "/transactions.txt"
        f = open(TRANSACTIONS,"a")
        f.write("Date: "+TODAY)
        f.write("\n")
        f.write("Type: "+TYPE)
        f.write("\n")
        f.write("Amount:"+str(AMOUNT))
        f.write("\n")
        f.write("Reason: "+REASON)
        f.write("\n")
        f.write("\n")
        f.close()

        BALANCE=PATH+ACCOUNT
        BALANCE += "/balance.txt"
        print BALANCE
        f = open(BALANCE,'r')
        x = f.read(1)
        f.close()
        x=float(x)
        if TYPE=="deposit":
            x=x+AMOUNT
            f = open(BALANCE,'w')
            f.write(x)
            f.close()
        if TYPE=="withdrawl":
            x=x-AMOUNT
            f = open(BALANCE,'w')
            f.write(x)
            f.close()

    
os.chdir(PATH1)

