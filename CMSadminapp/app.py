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

def editSliderItem(imageUrl, title, description, interval, oldTitle):
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
    myCursor.execute(f"""UPDATE sliderItems SET imageUrl="{imageUrl}", title="{title}", description="{description}", interval="{interval}" WHERE title="{oldTitle}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addSliderItem(imageUrl, title, description, interval):
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
    myCursor.execute(f"""INSERT INTO sliderItems (imageUrl, title, description, interval) VALUES ("{imageUrl}", "{title}", "{description}", "{interval}")""")
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

    Label(top, text="Interval: ").grid(row=4, column=0)
    intervalEdit = Spinbox(top, from_=0, to=100000)
    intervalEdit.grid(row=4, column=1)

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
        Button(top, text="Edit", command=lambda: editSliderItem(imgUrlEdit.get(), titleEdit.get(), descriptionEdit.get(), intervalEdit.get(), title)).grid(row=5, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addSliderItem(imgUrlEdit.get(), titleEdit.get(), descriptionEdit.get(), intervalEdit.get())).grid(row=5, column=1)


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




def deleteContentCard(title):

    MsgBox = tkinter.messagebox.askquestion ('Delete content card?', 'Are you sure you want to delete this content card?', icon='warning')
    if MsgBox == 'no':
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM contentCards WHERE title="{title}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no content card with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""DELETE FROM contentCards WHERE title="{title}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()

def editcontentCard(title, subtitle, content, imageURL, isImageOnLeftSide, oldTitle):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM contentCards WHERE title="{oldTitle}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is no content card with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""UPDATE contentCards SET title="{title}", subtitle="{subtitle}", content="{content}", imageURL="{imageURL}", isImageOnLeftSide="{isImageOnLeftSide}" WHERE title="{oldTitle}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addcontentCard(title, subtitle, content, imageURL, isImageOnLeftSide):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM contentCards WHERE title="{title}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) > 0:
        tkinter.messagebox.showerror(title="ERROR", message="There is already a content card with this title!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO contentCards (title, subtitle, content, imageURL, isImageOnLeftSide) VALUES ("{title}", "{subtitle}", "{content}", "{imageURL}", "{isImageOnLeftSide}")""")
    myConnection.commit()
    myConnection.close()
    top.destroy()
    onLoggedIn()
def showContentCardForm(title, mode):
    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM contentCards WHERE title="{title}" """)
        results = myCursor.fetchall()
        myConnection.commit()
        myConnection.close()
        if len(results) == 0:
            print(title, results)
            tkinter.messagebox.showerror(title="ERROR", message="There is no content card with this title!")
            return
    global top
    top = Toplevel(root, width=600, height=600)

    if mode == "edit":
        Label(top, text="Edit "+title).grid(row=0, column=1)
    if mode == "add":
        Label(top, text="Add").grid(row=0, column=1)

    Label(top, text="Title: ").grid(row=1, column=0)
    titleEdit = Entry(top)
    titleEdit.grid(row=1, column=1)

    Label(top, text="Subitle: ").grid(row=2, column=0)
    subtitleEdit = Entry(top)
    subtitleEdit.grid(row=2, column=1)

    Label(top, text="Content: ").grid(row=3, column=0)
    contentEdit = Entry(top)
    contentEdit.grid(row=3, column=1)

    Label(top, text="ImageURL: ").grid(row=4, column=0)
    imageUrlEdit = Entry(top)
    imageUrlEdit.grid(row=4, column=1)

    Label(top, text="Is image on left side: ").grid(row=5, column=0)
    isImgOnLeftSide = BooleanVar()
    isImgOnLeftSideEdit = Checkbutton(top, variable=isImgOnLeftSide, command=lambda: print(isImgOnLeftSide.get()))
    isImgOnLeftSideEdit.grid(row=5, column=1)

    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM contentCards WHERE title="{title}" """)
        results = myCursor.fetchall()
        print(results)
        print(results[0][0])
        myConnection.commit()
        myConnection.close()
        titleEdit.delete(0,END)
        titleEdit.insert(0,results[0][0])
        subtitleEdit.delete(0,END)
        subtitleEdit.insert(0,results[0][1])
        contentEdit.delete(0, END)
        contentEdit.insert(0, results[0][2])
        imageUrlEdit.delete(0, END)
        imageUrlEdit.insert(0, results[0][3])
        isImgOnLeftSide.set(1 if results[0][4] == 'True' else 0)
    if mode == "edit":
        Button(top, text="Edit", command=lambda: editcontentCard(titleEdit.get(), subtitleEdit.get(), contentEdit.get(), imageUrlEdit.get(), isImgOnLeftSide.get(), title)).grid(row=6, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addcontentCard(titleEdit.get(), subtitleEdit.get(), contentEdit.get(), imageUrlEdit.get(), isImgOnLeftSide.get())).grid(row=6, column=1)




def deleteHeaderItem(item):

    MsgBox = tkinter.messagebox.askquestion ('Delete header item?', 'Are you sure you want to delete this header item?', icon='warning')
    if MsgBox == 'no':
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM headerItems WHERE item="{item}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="This header item does not exist!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""DELETE FROM headerItems WHERE item="{item}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()

def editHeaderItem(item, oldItem):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM headerItems WHERE item="{oldItem}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="This header item does not exist!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""UPDATE headerItems SET item="{item}" WHERE item="{oldItem}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addHeaderItem(item):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM headerItems WHERE item="{item}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) > 0:
        tkinter.messagebox.showerror(title="ERROR", message="This header item already exists!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO headerItems (item) VALUES ("{item}")""")
    myConnection.commit()
    myConnection.close()
    top.destroy()
    onLoggedIn()
def showHeaderItemForm(item, mode):
    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM headerItems WHERE item="{item}" """)
        results = myCursor.fetchall()
        myConnection.commit()
        myConnection.close()
        if len(results) == 0:
            print(item, results)
            tkinter.messagebox.showerror(title="ERROR", message="This header item does not exist!")
            return
    global top
    top = Toplevel(root, width=600, height=600)

    if mode == "edit":
        Label(top, text="Edit "+item).grid(row=0, column=1)
    if mode == "add":
        Label(top, text="Add").grid(row=0, column=1)

    Label(top, text="Item: ").grid(row=1, column=0)
    itemEdit = Entry(top)
    itemEdit.grid(row=1, column=1)

    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM headerItems WHERE item="{item}" """)
        results = myCursor.fetchall()
        print(results)
        print(results[0][0])
        myConnection.commit()
        myConnection.close()
        itemEdit.delete(0,END)
        itemEdit.insert(0,results[0][0])
    if mode == "edit":
        Button(top, text="Edit", command=lambda: editHeaderItem(itemEdit.get(), item)).grid(row=2, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addHeaderItem(itemEdit.get())).grid(row=2, column=1)





def deleteFooterItem(item):

    MsgBox = tkinter.messagebox.askquestion ('Delete footer item?', 'Are you sure you want to delete this footer item?', icon='warning')
    if MsgBox == 'no':
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM footerItems WHERE item="{item}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="This footer item does not exist!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""DELETE FROM footerItems WHERE item="{item}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()

def editFooterItem(item, oldItem):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM footerItems WHERE item="{oldItem}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) == 0:
        tkinter.messagebox.showerror(title="ERROR", message="This footer item does not exist!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""UPDATE footerItems SET item="{item}" WHERE item="{oldItem}" """)
    myConnection.commit()
    myConnection.close()
    onLoggedIn()
def addFooterItem(item):
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM footerItems WHERE item="{item}" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    if len(results) > 0:
        tkinter.messagebox.showerror(title="ERROR", message="This footer item already exists!")
        return
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO footerItems (item) VALUES ("{item}")""")
    myConnection.commit()
    myConnection.close()
    top.destroy()
    onLoggedIn()
def showFooterItemForm(item, mode):
    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM footerItems WHERE item="{item}" """)
        results = myCursor.fetchall()
        myConnection.commit()
        myConnection.close()
        if len(results) == 0:
            print(item, results)
            tkinter.messagebox.showerror(title="ERROR", message="This footer item does not exist!")
            return
    global top
    top = Toplevel(root, width=600, height=600)

    if mode == "edit":
        Label(top, text="Edit "+item).grid(row=0, column=1)
    if mode == "add":
        Label(top, text="Add").grid(row=0, column=1)

    Label(top, text="Item: ").grid(row=1, column=0)
    itemEdit = Entry(top)
    itemEdit.grid(row=1, column=1)

    if mode == "edit":
        myConnection = sqlite3.connect('CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""SELECT * FROM footerItems WHERE item="{item}" """)
        results = myCursor.fetchall()
        print(results)
        print(results[0][0])
        myConnection.commit()
        myConnection.close()
        itemEdit.delete(0,END)
        itemEdit.insert(0,results[0][0])
    if mode == "edit":
        Button(top, text="Edit", command=lambda: editFooterItem(itemEdit.get(), item)).grid(row=2, column=1)
    if mode == "add":
        Button(top, text="Add", command=lambda: addFooterItem(itemEdit.get())).grid(row=2, column=1)




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

    Label(root, text="Edit content cards: ").grid(row=3, column=0)
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT title FROM contentCards""")
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    contentCards = ttk.Combobox(root)
    contentCards["values"] = list(map(lambda x: x[0], results))
    contentCards.grid(row=3, column=1)
    Button(root, text="Edit", command=lambda: showContentCardForm(contentCards.get(), "edit")).grid(row=3, column=2)
    Button(root, text="Delete", command=lambda: deleteContentCard(contentCards.get())).grid(row=3, column=3)
    Button(root, text="Add", command=lambda: showContentCardForm(contentCards.get(), "add")).grid(row=3, column=4)

    Label(root, text="Edit header items: ").grid(row=4, column=0)
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT item FROM headerItems""")
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    headerItems = ttk.Combobox(root)
    headerItems["values"] = list(map(lambda x: x[0], results))
    headerItems.grid(row=4, column=1)
    Button(root, text="Edit", command=lambda: showHeaderItemForm(headerItems.get(), "edit")).grid(row=4, column=2)
    Button(root, text="Delete", command=lambda: deleteHeaderItem(headerItems.get())).grid(row=4, column=3)
    Button(root, text="Add", command=lambda: showHeaderItemForm(headerItems.get(), "add")).grid(row=4, column=4)

    Label(root, text="Edit footer items: ").grid(row=5, column=0)
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT item FROM footerItems""")
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    footerItems = ttk.Combobox(root)
    footerItems["values"] = list(map(lambda x: x[0], results))
    footerItems.grid(row=5, column=1)
    Button(root, text="Edit", command=lambda: showFooterItemForm(footerItems.get(), "edit")).grid(row=5, column=2)
    Button(root, text="Delete", command=lambda: deleteFooterItem(footerItems.get())).grid(row=5, column=3)
    Button(root, text="Add", command=lambda: showFooterItemForm(footerItems.get(), "add")).grid(row=5, column=4)

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
