#The user will be asked to input a command
#When list of commands is determined remeber to add a list of them to test if
#the user is inputting the right thing, use a while loop like you have below for y/n
usrquery = input("What would you like to do? \nchange master directory enter cm\n")
#changing the the master directory
if usrquery == "cm":
    mstr_dir = input("insert new master directory\n")
correct_input = ("y","n")
#testing user input is correct
while usrquery == "cm":
    userquery_cm = input(mstr_dir + "\n is this correct? enter y or n\n")
    if userquery_cm == "y":
        print(mstr_dir)
        break
    if userquery_cm == "n":
        mstr_dir = input("insert correct master directory \n")
        continue
    if userquery_cm is not correct_input:
        userquery_cm = input("write y or n \n")
        continue

#storing mstr_dir variable
import json
data = mstr_dir
with open('mstr_dir.txt', 'w') as outfile:
    json.dump(data, outfile)
