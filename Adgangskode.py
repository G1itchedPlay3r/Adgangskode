import random
from turtle import up


#Adgangskode
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!?"

all = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(all, length))

#list to string
def listToString(s): 
    
    str1 = ""
    
    return (str1.join(s))
           
s = ["new kode: ", password]

#print to txt
with open ("koder.txt", "w") as testtxt:
    testtxt.write(listToString(s))

