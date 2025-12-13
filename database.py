import sqlite3
import sql_query
def create_user_table():
    with sqlite3.connect('users.db') as connection :
        cursor = connection.cursor()
        cursor.execute(sql_query.create_user_table)
        
def insert_user(id , name , username):
    with sqlite3.connect('users.db') as connection :
        cursor = connection.cursor()
        cursor.execute(sql_query.insert_query_user , (id , name , username))
        connection.commit()

def select_all_users():
    with sqlite3.connect('users.db') as connection :
        cursor = connection.cursor()
        cursor.execute(sql_query.select_query_allusers)
        return cursor.fetchall()
        
def select_user(id):
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(sql_query.select_one_user , (id,))
        return cursor.fetchone()
    
