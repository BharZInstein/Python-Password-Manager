#user data
conn = sqlite3.connect('pass_manager.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_data(
        username TEXT(20),
        master_pwd TEXT(20),
        PRIMARY KEY(username)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS user_data_storage(
        serial_no INTEGER,
        username TEXT(20),
        url TEXT,
        user_name TEXT,
        service_pwd TEXT,
        website_name TEXT,
        PRIMARY KEY(serial_no)
        FOREIGN KEY(M_username)
            REFERENCES user_data(username)
    )""")

conn.commit()

conn.close()

