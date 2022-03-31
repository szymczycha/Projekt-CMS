import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("400x300")


def deleteSliderItem(title):
    MsgBox = tkinter.messagebox.askquestion('Delete Slider Item?', 'Are you sure you want to delete this slider item?', icon='warning')
    if MsgBox == 'no':
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="{title}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no slider item with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""DELETE FROM sliderItems WHERE title="{title}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()

def editSliderItem(imageUrl, title, description, oldTitle):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="{oldTitle}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no slider item with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""UPDATE sliderItems SET imageUrl="{imageUrl}", title="{title}", description="{description}" WHERE title="{oldTitle}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addSliderItem(imageUrl, title, description):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="{title}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) > 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is already a slider item with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO sliderItems (imageUrl, title, description) VALUES ("{imageUrl}", "{title}", "{description}")""")
    myConnection.commit()
    myConnection.close()
    top.destroy()
    onLoggedIn()
def showSliderItemForm(title, mode):
    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="{title}" """)
        results = myCursor.fetchall()
        myConnection.commit()
        myConnection.close()
        if len(results) == 0:
            print(title, results)
            tkinter.messagebox.showerror(title="ERROR", message="There is no slider items with this title!")
            return
    global top
    top = Toplevel(root, width=600, height=600)

    if mode == "edit":
        Label(top, text="Edit "+title).grid(row=0, column=1)
    if mode == "add":
        Label(top, text="Add").grid(row=0, column=1)

    Label(top, text="Image URL: ").grid(row=1, column=0)
    imgUrlEdit = Entry(top)
    imgUrlEdit.grid(row=1, column=1)

    Label(top, text="Title: ").grid(row=2, column=0)
    titleEdit = Entry(top)
    titleEdit.grid(row=2, column=1)

    Label(top, text="Description: ").grid(row=3, column=0)
    descriptionEdit = Entry(top)
    descriptionEdit.grid(row=3, column=1)

    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="{title}" """)
        results = myCursor.fetchall()
        print(results)
        print(results[0][0])
        myConnection.commit()
        myConnection.close()
        imgUrlEdit.delete(0,END)
        imgUrlEdit.insert(0,results[0][0])
        titleEdit.delete(0,END)
        titleEdit.insert(0,results[0][1])
        descriptionEdit.delete(0,END)
        descriptionEdit.insert(0,results[0][2])
    if mode == "edit":
        Button(top, text="Edit", command=lambda: editSliderItem(imgUrlEdit.get(), titleEdit.get(), descriptionEdit.get(), title)).grid(row=5, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addSliderItem(imgUrlEdit.get(), titleEdit.get(), descriptionEdit.get())).grid(row=5, column=1)


def deleteNews(title):

    MsgBox = tkinter.messagebox.askquestion ('Delete news?','Are you sure you want to delete these news?',icon = 'warning')
    if MsgBox == 'no':
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM news WHERE title="{title}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no user with this username!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""DELETE FROM news WHERE title="{title}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()

def editNews(header, title, content, buttonText, oldTitle):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM news WHERE title="{oldTitle}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no news with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""UPDATE news SET header="{header}", title="{title}", content="{content}", buttonText="{buttonText}" WHERE title="{oldTitle}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addNews(header, title, content, buttonText):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM news WHERE title="{title}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) > 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is already news with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO news (header, title, content, buttonText) VALUES ("{header}", "{title}", "{content}", "{buttonText}")""")
    myConnection.commit()
    myConnection.close()
    top.destroy()
    onLoggedIn()
def showNewsForm(title, mode):
    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM news WHERE title="{title}" """)
        results = myCursor.fetchall()
        myConnection.commit()
        myConnection.close()
        if len(results) == 0:
            print(title, results)
            tkinter.messagebox.showerror(title="ERROR", message="There is no news with this title!")
            return
    global top
    top = Toplevel(root, width=600, height=600)

    if mode == "edit":
        Label(top, text="Edit "+title).grid(row=0, column=1)
    if mode == "add":
        Label(top, text="Add").grid(row=0, column=1)

    Label(top, text="Header: ").grid(row=1, column=0)
    headerEdit = Entry(top)
    headerEdit.grid(row=1, column=1)

    Label(top, text="Title: ").grid(row=2, column=0)
    titleEdit = Entry(top)
    titleEdit.grid(row=2, column=1)

    Label(top, text="Content: ").grid(row=3, column=0)
    contentEdit = Entry(top)
    contentEdit.grid(row=3, column=1)


    Label(top, text="Button text: ").grid(row=4, column=0)
    buttonTextEdit = Entry(top)
    buttonTextEdit.grid(row=4, column=1)

    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM news WHERE title="{title}" """)
        results = myCursor.fetchall()
        print(results)
        print(results[0][0])
        myConnection.commit()
        myConnection.close()
        headerEdit.delete(0,END)
        headerEdit.insert(0,results[0][0])
        titleEdit.delete(0,END)
        titleEdit.insert(0,results[0][1])
        contentEdit.delete(0,END)
        contentEdit.insert(0,results[0][2])
        buttonTextEdit.delete(0,END)
        buttonTextEdit.insert(0,results[0][3])
    if mode == "edit":
        Button(top, text="Edit", command=lambda: editNews(headerEdit.get(), titleEdit.get(), contentEdit.get(), buttonTextEdit.get(), title)).grid(row=5, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addNews(headerEdit.get(), titleEdit.get(), contentEdit.get(), buttonTextEdit.get())).grid(row=5, column=1)




def editUser(username, password, usertype, oldUsername):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM users WHERE username="{oldUsername}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no user with this username!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""UPDATE users SET username="{username}", password="{password}", userType="{usertype}" WHERE username="{oldUsername}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()

def deleteUser(username):
    MsgBox = tkinter.messagebox.askquestion ('Delete user','Are you sure you want to delete this user?',icon = 'warning')
    if MsgBox == 'no':
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM users WHERE username="{username}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no user with this username!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""DELETE FROM users WHERE username="{username}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addNewUser(username, password, usertype):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM users WHERE username="{username}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) > 0:
        tkinter.messagebox.showerror(title="ERROR", message="This username already exists!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO users (username, password, userType) VALUES ("{username}", "{password}", "{usertype}")""")
    myConnection.commit()
    myConnection.close()
    top.destroy()
    onLoggedIn()
def showUserForm(name, mode):
    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM users WHERE username="{name}" """)
        results = myCursor.fetchall()
        myConnection.commit()
        myConnection.close()
        if len(results) == 0:
            tkinter.messagebox.showerror(title="ERROR", message="There is no user with this username!")
            return
    global top
    top = Toplevel(root, width=600, height=600)

    if mode == "edit":
        Label(top, text="Edit "+name).grid(row=0, column=1)
    if mode == "add":
        Label(top, text="Add").grid(row=0, column=1)

    Label(top, text="Username: ").grid(row=1, column=0)
    usernameEdit = Entry(top)
    usernameEdit.grid(row=1, column=1)

    Label(top, text="Password: ").grid(row=2, column=0)
    passwordEdit = Entry(top, show="*")
    passwordEdit.grid(row=2, column=1)

    Label(top, text="User type: ").grid(row=3, column=0)
    userTypeEdit = ttk.Combobox(top)
    userTypeEdit['state'] = "readonly";
    userTypeEdit["values"] = ["moderator", "user", "admin"]
    userTypeEdit.set("user")
    userTypeEdit.grid(row=3, column=1)

    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM users WHERE username="{name}" """)
        results = myCursor.fetchall()
        print(results)
        print(results[0][0])
        myConnection.commit()
        myConnection.close()
        usernameEdit.delete(0,END)
        usernameEdit.insert(0,results[0][0])
        passwordEdit.delete(0,END)
        passwordEdit.insert(0,results[0][1])
        userTypeEdit.set(results[0][2])
    if mode == "edit":
        Button(top, text="Edit", command=lambda: editUser(usernameEdit.get(), passwordEdit.get(), userTypeEdit.get(), name)).grid(row=4, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addNewUser(usernameEdit.get(), passwordEdit.get(), userTypeEdit.get())).grid(row=4, column=1)


def onLoggedIn():

    for child in root.winfo_children():
        child.destroy()

    Label(root, text="Edit user: ").grid(row=0, column=0)
    userSelect = ttk.Combobox(root)
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT username FROM users""")
    results = myCursor.fetchall()
    myConnection.close()
    print(results)
    userSelect["values"] = list(map(lambda x: x[0], results))
    print("val:", userSelect["values"])
    userSelect.grid(row=0, column=1)
    Button(root, text="Edit", command=lambda: showUserForm(userSelect.get(), "edit")).grid(row=0, column=2)
    Button(root, text="Delete", command=lambda: deleteUser(userSelect.get())).grid(row=0, column=3)
    Button(root, text="Add", command=lambda: showUserForm(userSelect.get(), "add")).grid(row=0, column=4)

    Label(root, text="Edit news: ").grid(row=1, column=0)
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT title FROM news""")
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    optionMenu = ttk.Combobox(root)
    optionMenu["values"] = list(map(lambda x: x[0], results))
    optionMenu.grid(row=1, column=1)
    Button(root, text="Edit", command=lambda: showNewsForm(optionMenu.get(), "edit")).grid(row=1, column=2)
    Button(root, text="Delete", command=lambda: deleteNews(optionMenu.get())).grid(row=1, column=3)
    Button(root, text="Add", command=lambda: showNewsForm(optionMenu.get(), "add")).grid(row=1, column=4)

    Label(root, text="Edit slider items: ").grid(row=2, column=0)
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT title FROM sliderItems""")
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    sliderItems = ttk.Combobox(root)
    sliderItems["values"] = list(map(lambda x: x[0], results))
    sliderItems.grid(row=2, column=1)
    Button(root, text="Edit", command=lambda: showSliderItemForm(sliderItems.get(), "edit")).grid(row=2, column=2)
    Button(root, text="Delete", command=lambda: deleteSliderItem(sliderItems.get())).grid(row=2, column=3)
    Button(root, text="Add", command=lambda: showSliderItemForm(sliderItems.get(), "add")).grid(row=2, column=4)

def logIn():
    # tworzenie bazy lub połączenie z istniejącą bazą
    myConnection = sqlite3.connect('CMS.db')
    # tworzenie kursora do bazy
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM users WHERE username="{usernameEntry.get()}" AND password="{passwordEntry.get()}" AND userType="admin" """)
    results = myCursor.fetchall()
    myConnection.close()
    if len(results) > 0:
        print("logged in")
        onLoggedIn()

Label(root, text="Admin panel").grid(row=0, column=1)
Label(root, text="Username: ").grid(row=1, column=0)
usernameEntry = Entry(root)
usernameEntry.grid(row=1, column=1)

Label(root, text="Password: ").grid(row=2, column=0)
passwordEntry = Entry(root, show="*")
passwordEntry.grid(row=2, column=1)

loginButton = Button(root, text="Log in!", command=logIn)
loginButton.grid(row=3, column=1)




root.mainloop()
