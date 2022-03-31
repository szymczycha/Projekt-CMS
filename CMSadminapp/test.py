
import sqlite3

myConnection = sqlite3.connect("CMS.db")
myCursor = myConnection.cursor()
myCursor.execute("""SELECT * FROM news""")
print(myCursor.fetchall())
myConnection.commit()
myConnection.close()