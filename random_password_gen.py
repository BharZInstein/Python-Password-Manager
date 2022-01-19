import random
import string
def passgen(): 
    length = 6

    small = string.ascii_lowercase 
    big = string.ascii_uppercase
    dig = string.digits
    symbols = string.punctuation

    TPass1 = random.sample(small,1)
    TPass2 = random.sample(big,1)
    TPass3 = random.sample(dig,1) 
    TPass4 = random.sample(symbols,1)

    LPass = TPass1 + TPass2 + TPass3 + TPass4

    All = small + big + dig + symbols   

    BPass = random.sample(All,length)

    Pass = LPass + BPass
    random.shuffle(Pass)

    Password = "" .join(Pass)
    return Password