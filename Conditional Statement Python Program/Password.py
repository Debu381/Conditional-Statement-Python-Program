#Write a Python program to check the validity of a password (input from users).
#Validation :
#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
##At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters

import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")