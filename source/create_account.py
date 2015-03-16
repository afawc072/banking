import os

print"Enter the acount type i.e ( Credit, Cheque, Saving):"
ACCOUNT_NAME=raw_input()
PATH=os.getcwd()
#add bank to path
PATH+="/bank/"
PATH+=ACCOUNT_NAME
os.mkdir(PATH)

f = open (PATH+"/balance.txt", 'a')
f.write("0")
f.close()
f = open (PATH+"/transactions.txt", 'a')
f.close()


    
