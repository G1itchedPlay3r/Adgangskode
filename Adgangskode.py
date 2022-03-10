import random
from turtle import up

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!?"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
print (password)

