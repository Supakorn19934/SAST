import sqlite3

def create_connection():
    conn = sqlite3.connect(':memory:')
    return conn

def create_table(conn):
    sql_create_table = """ CREATE TABLE users (
                                id integer PRIMARY KEY,
                                username text NOT NULL,
                                password text NOT NULL
                            ); """
    conn.execute(sql_create_table)
    conn.commit()

def add_user(conn, username, password):
    sql_insert_user = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    conn.execute(sql_insert_user)
    conn.commit()

def main():
    conn = create_connection()
    create_table(conn)
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    add_user(conn, username, password)
    print("User added successfully")

if __name__ == '__main__':
    main()
