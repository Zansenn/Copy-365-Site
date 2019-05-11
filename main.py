#this is the central module that will call the other modules
#here we will list all possible user commands

#import sys
print(sys.path)
sys.path.append('C:\\Users\\Naz Sen\\Documents\\Programs\\Programming\\Copy 365 Site')
correct_command = ("cdir", "cm", "end")
userquery = 0
usercopy = 0
while userquery is not correct_command:
    userquery= input('''What would you like to do? \nchange master directory enter cm\n copy from master directory to a new location type cdir\n leave type end \n''')
    if userquery == "end":
        break
        end()
    if userquery == "cdir":
        #usercopy == "cdir"
        import copyfrommstr.py
        continue
    if userquery == "cm":
        userquery = 0
        import assignmstr.py
        continue
