import sqlite3

def create_admin_table():
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\admin.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE  admin
        (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def check_admin(email, password):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\admin.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM ADMIN WHERE email= '{email}' and password='{password}'")

    data = cursor.fetchone()

    conn.commit()
    conn.close()

    return data
    
def is_admin(email, password):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\admin.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM ADMIN WHERE email= '{email}' and password='{password}'")

    data = cursor.fetchone()

    conn.commit()
    conn.close()

    return data
    
def add_admin(firstname, lastname, email, password):
    conn = sqlite3.connect('c:\\Users\\sharm\\OneDrive\\Desktop\\accounting\\admin.db')

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO ADMIN VALUES ('{firstname}','{lastname}','{email}','{password}')")

    conn.commit()
    conn.close()
    return 0

# add_admin('Anil', 'Sharma', 'anil@gmail.com','12345678')