import hashlib

password="password"
def hashPassword(input):
    hash=hashlib.md5(input)
    hash = hash.hexdigest()
    return hash
print(hashPassword(password.encode('utf=8')))

