from cgi import test
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
    
    
    str1 = "\n" 
    
    
    return (str1.join(s))
           
s = [password]
print(listToString(s)) 

#print to txt
file = open ("koder.txt", "a+")

file.write(listToString(s))

file.close()