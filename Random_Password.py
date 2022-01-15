import random
import pyperclip
def randpass():

     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!$#()*&1234567890"

     password = ""
     while True:
          password_len = int(input("what is the length of your password:"))
          for x in range(0,password_len):
               password_chars = random.choice(chars)
               password = password + password_chars
          return password          