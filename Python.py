import sqlite3

def get_user_data(user_id):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    
    # ช่องโหว่ SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    result = cursor.fetchone()
    connection.close()
    
    return result

# เรียกใช้ฟังก์ชัน
# print(get_user_data("1 OR 1=1"))
