from users import User
import sqlite3
import os

class DB():
    def __init__(self):
        if os.path.exists('users.db') == False:
            self.createBD()

    def createBD(self):
        try:
            sqlite_connection = sqlite3.connect('users.db')
            cursor = sqlite_connection.cursor()
            cursor.execute('''CREATE TABLE users (
                                name text PRIMARY KEY,
                                password text NOT NULL UNIQUE);''')
            # cursor.fetchall()
            print('DB is created')
        except sqlite3.Error as error:
            print('No connection to DB', error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print('DB is closed')

    def addToDB(user):
        try:
            sqlite_connection = sqlite3.connect('users.db')
            cursor = sqlite_connection.cursor()
            cursor.execute("""INSERT INTO users 
                           VALUES (?,?)""", [user.getName(), user.getPassword()])    

            # cursor.fetchall()
            sqlite_connection.commit()
            print(user.getName(), ' is added.')
        except sqlite3.Error as error:
            print("Not add to DB")
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print('DB is closed')

    def removeToDB(user):
        try:
            sqlite_connection = sqlite3.connect('users.db')
            cursor = sqlite_connection.cursor()
            cursor.execute('DELETE FROM users WHERE name = ?',[user.getName()])
            sqlite_connection.commit()
            print(user.getName(), ' is deleted.')
        except sqlite3.Error as error:
            print(user.getName(), ' Not remove in DB!')
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print('DB is closed')


# user = User("Jerry", "newpassword")
# DB()
# DB.addToDB(user)
# DB.removeToDB(user)