import sqlite3

# tworzenie bazy lub połączenie z istniejącą bazą
myConnection = sqlite3.connect('CMS.db')
# tworzenie kursora do bazy
myCursor = myConnection.cursor()

# tworzenie tabeli
myCursor.execute("""CREATE TABLE IF NOT EXISTS users(
            username text,
            password text,
            userType text
            )""")

# tworzenie tabeli
myCursor.execute("""CREATE TABLE IF NOT EXISTS news(
            header text,
            title text,
            content text,
            buttonText text
            )""")

# tworzenie tabeli
myCursor.execute("""CREATE TABLE IF NOT EXISTS sliderItems(
            imageUrl text,
            title text,
            description text,
            interval integer
            )""")

myCursor.execute("""CREATE TABLE IF NOT EXISTS contentCards(
            title text,
            subtitle text,
            content text,
            imageUrl text,
            isImageOnLeftSide boolean
            )""")

myCursor.execute("""CREATE TABLE IF NOT EXISTS headerItems(
            item text
            )""")

myCursor.execute("""CREATE TABLE IF NOT EXISTS footerItems(
            item text
            )""")

myCursor.execute("""CREATE TABLE IF NOT EXISTS themes(
            id integer PRIMARY KEY AUTOINCREMENT,
            name text,
            mainBackgroundColor text,
            secondaryBackgroundColor text,
            newsHeaderBackgroundColor text,
            mainTextColor text,
            secondaryTextColor text
            )""")

# zapisywanie zmian w bazie
myConnection.commit()

# kończenie połączenia z bazą
myConnection.close()

myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM users WHERE username="admin" """)
results = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("""INSERT INTO users (username, password, userType) VALUES ("admin", "admin", "admin")""")
    myConnection.commit()
    myConnection.close()