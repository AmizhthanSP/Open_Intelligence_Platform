import mysql.connector

db_config = {
    'host': 'localhost', 
    'user': 'root',  
    'password': 'ConceptVines$@SX#21', 
    'database': 'test_db'  
}

try:
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print('Connected to MySQL database')
        query = "SELECT * FROM bausecases"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL: {e}')

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('Connection to MySQL database closed')
