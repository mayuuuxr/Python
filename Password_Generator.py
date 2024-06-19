import string
import random
from csv import writer


def Pass():
    s1= string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    Platform = input("Enter the name of your platform : ")
    PassLength = int(input("Enter the length of Your Password : "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    Password = ("".join(s[0:PassLength]))
    print(Password)
    passdata = [Platform,Password]
    with open('pass.csv','a') as f:
     writedata = writer(f)    
     writedata.writerow(passdata)  

Pass()    