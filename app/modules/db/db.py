import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        database='db_ecommerce',
        password='admin1234'
    )
    return connection
