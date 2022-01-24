import hashlib
#Encrypting(hashing) the password
def make_pw_hash(password):
    password=password.encode('utf-8')
    hash1= hashlib.md5(password)
    hash1= hash1.hexdigest()
    return hash1
#Vefifying for user inputed password
def check_pw_hash(password, hash2):
    if make_pw_hash(password)== hash2:
        return True
    else:
        return False
