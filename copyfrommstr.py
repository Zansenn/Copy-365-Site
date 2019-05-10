#the user will need to approve the mstr_dir this will be read from mstr_dir.txt
#once approved they will need to select the director that they will be copying
import json
import shutil
correct_input = ("y","n")

usercopy = input ("What would you like to do? to copy from master directory to new director type cdir\n")
if usercopy == "cdir":
    with open('mstr_dir.txt') as json_file:
        mstr_dir = json.load(json_file)
        print(mstr_dir)

print("above is the directory you will copy to: \n")
#testing that the user has inputted the correct information
while correct_input == ("y","n"):
    if usercopy == ("y"):
        break
    if usercopy == "n":
        #run the assignmstr.py. You need to add this in so for now "n" wont work
        usercopy =input("please write y/n\n")
        continue
    if usercopy is not correct_input:
        usercopy = input("please write y/n\n")
        continue
print(mstr_dir)
trgt_dir = input("please input target directory\n")
#copy the files
shutil.copy(mstr_dir, trgt_dir)
exit()
