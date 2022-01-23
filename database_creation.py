import sqlite3
#user data
conn = sqlite3.connect('pass_manager.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_data(
        M_username TEXT(20) UNIQUE NOT NULL,
        master_pwd TEXT(20) NOT NULL,
        PRIMARY KEY(M_username)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS user_data_storage(
        M_username TEXT(20) NOT NULL,
        url TEXT NOT NULL,
        user_name TEXT NOT NULL, 
        service_pwd TEXT NOT NULL,
        website_name TEXT NOT NULL,   
        FOREIGN KEY(M_username) REFERENCES user_data(M_username))""")

c.execute("""CREATE TABLE IF NOT EXISTS admin_user_data(
        admin_username TEXT(20) UNIQUE NOT NULL,
        admin_pwd TEXT(20) NOT NULL,
        PRIMARY KEY(admin_username)
    )""")



c.execute("""INSERT INTO admin_user_data
             (admin_username, admin_pwd) 
             VALUES
               ('adhiraj','1234'),
               ('bharghav','1234'),
               ('kanish','1234'),
               ('seyan','1234');
      """)

                

conn.commit()

conn.close()
