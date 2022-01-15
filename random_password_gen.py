import random
import string

length = 10

small = string.ascii_lowercase 
big = string.ascii_uppercase
dig = string.digits
symbols = string.punctuation

all = small + big + dig + symbols

Pass = random.sample(all,length)

password = "".join(Pass)

print(password)

