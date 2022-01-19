m_username=''
def usrStore(usr):
    global m_username
    m_username=m_username+usr
    print(usrCall())
    return None
def usrCall():
    return m_username