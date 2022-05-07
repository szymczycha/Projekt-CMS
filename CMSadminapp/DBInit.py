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
            buttonText text,
            article text,
            id integer PRIMARY KEY AUTOINCREMENT
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

myCursor.execute("""CREATE TABLE IF NOT EXISTS comments(
            articleId integer,
            author text,
            date text,
            content text 
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


myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM themes WHERE name="default" """)
results = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("""INSERT INTO themes (name, mainBackgroundColor, secondaryBackgroundColor, newsHeaderBackgroundColor, mainTextColor, secondaryTextColor) VALUES ("default","#303030", "#d0d0d0", "#909090", "#d0d0d0", "#000000")""")
    myCursor.execute("""INSERT INTO themes (name, mainBackgroundColor, secondaryBackgroundColor, newsHeaderBackgroundColor, mainTextColor, secondaryTextColor) VALUES ("green","#007A18", "#50D317", "#00B33E", "#F2F2F2", "#000000")""")
    myConnection.commit()
    myConnection.close()

    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM themes WHERE name="default" """)
    results = myCursor.fetchall()
    myConnection.commit()
    myConnection.close()
    with open("./config/selectedTheme.txt", "w") as f:
        f.write(str(results[0][0]))



myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM news WHERE title="News template!" """)
results1 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM news WHERE title="News template2!" """)
results2 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM news WHERE title="News template3!" """)
results3 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results1) == 0 and len(results2) == 0 and len(results3) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("""INSERT INTO news (header, title, content, buttonText, article) VALUES (
        "Template Header",
        "News template!", 
        "Wow this is so interesting!", 
        "Click me!",
        "This is the article. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed libero justo, convallis et neque quis, tempor suscipit mauris. Cras consequat ornare leo sit amet euismod. Praesent suscipit justo quis nisi lobortis, eget accumsan dui aliquam. Curabitur venenatis sodales ultrices. Morbi tristique lacus turpis, id sodales turpis egestas ac. Sed auctor, est et pretium sagittis, lectus dolor auctor felis, at suscipit justo ipsum vitae sem. Duis arcu massa, mattis fringilla augue nec, pellentesque ultricies odio. Integer velit elit, sollicitudin eget magna vitae, imperdiet mollis libero. Fusce odio odio, scelerisque bibendum dolor id, mattis mattis mi. Donec euismod elit vitae tempus vulputate. Sed placerat ornare nisl. Curabitur sit amet luctus nibh. Duis non orci est. Nunc quis feugiat nibh. Donec sed est bibendum, mollis quam ut, lobortis augue.")""")
    myCursor.execute("""INSERT INTO news (header, title, content, buttonText, article) VALUES (
        "Template Header",
        "News template2!", 
        "Wow this is so interesting!", 
        "Click me!",
        "This is the article. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed libero justo, convallis et neque quis, tempor suscipit mauris. Cras consequat ornare leo sit amet euismod. Praesent suscipit justo quis nisi lobortis, eget accumsan dui aliquam. Curabitur venenatis sodales ultrices. Morbi tristique lacus turpis, id sodales turpis egestas ac. Sed auctor, est et pretium sagittis, lectus dolor auctor felis, at suscipit justo ipsum vitae sem. Duis arcu massa, mattis fringilla augue nec, pellentesque ultricies odio. Integer velit elit, sollicitudin eget magna vitae, imperdiet mollis libero. Fusce odio odio, scelerisque bibendum dolor id, mattis mattis mi. Donec euismod elit vitae tempus vulputate. Sed placerat ornare nisl. Curabitur sit amet luctus nibh. Duis non orci est. Nunc quis feugiat nibh. Donec sed est bibendum, mollis quam ut, lobortis augue.")""")
    myCursor.execute("""INSERT INTO news (header, title, content, buttonText, article) VALUES (
        "Template Header",
        "News template3!", 
        "Wow this is so interesting!", 
        "Click me!",
        "This is the article. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed libero justo, convallis et neque quis, tempor suscipit mauris. Cras consequat ornare leo sit amet euismod. Praesent suscipit justo quis nisi lobortis, eget accumsan dui aliquam. Curabitur venenatis sodales ultrices. Morbi tristique lacus turpis, id sodales turpis egestas ac. Sed auctor, est et pretium sagittis, lectus dolor auctor felis, at suscipit justo ipsum vitae sem. Duis arcu massa, mattis fringilla augue nec, pellentesque ultricies odio. Integer velit elit, sollicitudin eget magna vitae, imperdiet mollis libero. Fusce odio odio, scelerisque bibendum dolor id, mattis mattis mi. Donec euismod elit vitae tempus vulputate. Sed placerat ornare nisl. Curabitur sit amet luctus nibh. Duis non orci est. Nunc quis feugiat nibh. Donec sed est bibendum, mollis quam ut, lobortis augue.")""")

    myConnection.commit()
    myConnection.close()


myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="Template 1" """)
results1 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="Template 2" """)
results2 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM sliderItems WHERE title="Template 3" """)
results3 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results1) == 0 and len(results2) == 0 and len(results3) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("""INSERT INTO sliderItems (imageUrl, title, description, interval) VALUES (
        "https://picsum.photos/id/523/1920/500",
        "Template 1", 
        "Wow cool photo", 
        5000)""")
    myCursor.execute("""INSERT INTO sliderItems (imageUrl, title, description, interval) VALUES (
        "https://picsum.photos/id/223/1920/500",
        "Template 2", 
        "Wow cool photo", 
        5000)""")
    myCursor.execute("""INSERT INTO sliderItems (imageUrl, title, description, interval) VALUES (
        "https://picsum.photos/id/342/1920/500",
        "Template 3", 
        "Wow cool photo", 
        5000)""")

    myConnection.commit()
    myConnection.close()

myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM contentCards WHERE title="Template 1" """)
results1 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM contentCards WHERE title="Template 2" """)
results2 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM contentCards WHERE title="Template 3" """)
results3 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results1) == 0 and len(results2) == 0 and len(results3) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""INSERT INTO contentCards (title, subtitle, content, imageURL, isImageOnLeftSide) VALUES (
        "Template 1",
        "This is a subtitle",
        "This is a really nice content card. Donec posuere neque faucibus dui congue, vel tempor est fringilla. Integer ullamcorper consequat enim, sit amet venenatis sapien ornare quis. Duis at sodales sapien, at blandit erat. Aenean tempus tempor dolor, quis dictum ex congue non. Proin ex sapien, cursus eget dignissim sit amet, ultricies eget eros. Fusce luctus diam sed mi placerat suscipit. Sed massa massa, scelerisque eu massa nec, venenatis egestas ex. Vestibulum vitae quam ac magna sodales sollicitudin gravida id velit.", 
        "https://picsum.photos/id/123/500/500",
        "{True}" )""")

    myCursor.execute(f"""INSERT INTO contentCards (title, subtitle, content, imageURL, isImageOnLeftSide) VALUES (
        "Template 2",
        "This is a subtitle",
        "This is a really nice content card. Donec posuere neque faucibus dui congue, vel tempor est fringilla. Integer ullamcorper consequat enim, sit amet venenatis sapien ornare quis. Duis at sodales sapien, at blandit erat. Aenean tempus tempor dolor, quis dictum ex congue non. Proin ex sapien, cursus eget dignissim sit amet, ultricies eget eros. Fusce luctus diam sed mi placerat suscipit. Sed massa massa, scelerisque eu massa nec, venenatis egestas ex. Vestibulum vitae quam ac magna sodales sollicitudin gravida id velit.", 
        "https://picsum.photos/id/322/500/500",
        "{False}" )""")

    myCursor.execute(f"""INSERT INTO contentCards (title, subtitle, content, imageURL, isImageOnLeftSide) VALUES (
        "Template 3",
        "This is a subtitle",
        "This is a really nice content card. Donec posuere neque faucibus dui congue, vel tempor est fringilla. Integer ullamcorper consequat enim, sit amet venenatis sapien ornare quis. Duis at sodales sapien, at blandit erat. Aenean tempus tempor dolor, quis dictum ex congue non. Proin ex sapien, cursus eget dignissim sit amet, ultricies eget eros. Fusce luctus diam sed mi placerat suscipit. Sed massa massa, scelerisque eu massa nec, venenatis egestas ex. Vestibulum vitae quam ac magna sodales sollicitudin gravida id velit.", 
        "https://picsum.photos/id/155/500/500",
        "{True}" )""")

    myConnection.commit()
    myConnection.close()


myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM headerItems WHERE item="Features" """)
results1 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM headerItems WHERE item="About" """)
results2 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM headerItems WHERE item="FAQ" """)
results3 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results1) == 0 and len(results2) == 0 and len(results3) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("""INSERT INTO headerItems (item) VALUES ("Features")""")
    myCursor.execute("""INSERT INTO headerItems (item) VALUES ("About")""")
    myCursor.execute("""INSERT INTO headerItems (item) VALUES ("FAQ")""")
    myConnection.commit()
    myConnection.close()

myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM footerItems WHERE item="Features" """)
results1 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM footerItems WHERE item="About" """)
results2 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
myConnection = sqlite3.connect('CMS.db')
myCursor = myConnection.cursor()
myCursor.execute(f"""SELECT * FROM footerItems WHERE item="FAQ" """)
results3 = myCursor.fetchall()
myConnection.commit()
myConnection.close()
if len(results1) == 0 and len(results2) == 0 and len(results3) == 0:
    myConnection = sqlite3.connect('CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("""INSERT INTO footerItems (item) VALUES ("Features")""")
    myCursor.execute("""INSERT INTO footerItems (item) VALUES ("About")""")
    myCursor.execute("""INSERT INTO footerItems (item) VALUES ("FAQ")""")
    myConnection.commit()
    myConnection.close()