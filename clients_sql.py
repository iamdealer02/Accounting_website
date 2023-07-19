import sqlite3



def create_user_table():
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\users.db')
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist and an admin table for the admins
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users 
        (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            verification INT  NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def add_user(firstname, lastname, email, password,verification):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\users.db')

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO USERS VALUES ('{firstname}','{lastname}','{email}','{password}',{verification})")

    conn.commit()
    conn.close()
    return 0

def check_user(email,password):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\users.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM USERS WHERE email= '{email}' and password='{password}'")

    data = cursor.fetchone()

    conn.commit()
    conn.close()

    return data

def check_verification(email,password):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\users.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT verification FROM USERS WHERE email= '{email}' and password='{password}'")

    data = cursor.fetchone()

    conn.commit()
    conn.close()

    return data[0]

def verification_done(email, password):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\users.db')

    cursor = conn.cursor()

    cursor.execute(f"UPDATE USERS SET verification = 1  WHERE email= '{email}' and password='{password}'")



    conn.commit()
    conn.close()


