import sqlite3

# conn = sqlite3.connect('dbaza.db')

# # Kursor yaratish
# cursor = conn.cursor()

# # Ma'lumot qo'shish
# cursor.execute('''INSERT INTO ichimliklar (nomi, narxi)
#                   VALUES (?, ?)''', ('CocaCola', 14000))

# # Yana bir ma'lumot qo'shish
# cursor.execute('''INSERT INTO ichimliklar (nomi, narxi)
#                   VALUES (?, ?)''', ('Fanta', 13000))

# # O'zgarishlarni saqlash
# conn.commit()

# # Bazani yopish
# conn.close()




def UsersAdd(title, username):
    try:
        sqliteConnection = sqlite3.connect('dbaza.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """
        INSERT INTO telegram_bot_users (title, username) 
                                 VALUES (?, ?)
        ON CONFLICT(username) DO UPDATE SET
        title=excluded.title,
        username=excluded.username
        """  # 'telegram_id' o'rniga 'username' ni ishlatyapmiz, agar 'username' noyob bo'lsa.
        cursor.execute(sqlite_insert_query, (title, username))

        sqliteConnection.commit()
        print("Record inserted/updated successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('dbaza.db')

# Kursor yaratish
cursor = conn.cursor()

# Jadval yaratish
cursor.execute('''CREATE TABLE IF NOT EXISTS taomlar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nomi TEXT NOT NULL,
                    narxi REAL NOT NULL
                )''')

# O'zgarishlarni saqlash
conn.commit()

# Bazani yopish
conn.close()

def Food_Sql():
    try:
        sqliteConnection = sqlite3.connect('dbaza.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM taomlar"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def Menyu_Sql():
    try:
        sqliteConnection = sqlite3.connect('dbaza.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM menyu"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows if totalRows else []  # Bo'sh ro'yxat qaytariladi

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        return []  # Xato bo'lsa, bo'sh ro'yxat qaytariladi

    finally:
        if sqliteConnection:
            sqliteConnection.close()



def Ichimliklar():
    try:
        sqliteConnection = sqlite3.connect('dbaza.db')
        cursor = sqliteConnection.cursor()

        # Ichimliklarni olish uchun tegishli SQL so'rov
        sqlite_select_query = """SELECT * FROM taomlar WHERE kategoriya = 'ichimliklar'"""  
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def Taomlar():
    try:
        sqliteConnection = sqlite3.connect('dbaza.db')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * FROM taomlar Where id = 1"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()



