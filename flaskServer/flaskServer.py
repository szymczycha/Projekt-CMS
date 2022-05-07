from flask import Flask, render_template, request, jsonify, make_response, send_from_directory
import sqlite3


app = Flask(__name__)
app.config["SECRET_KEY"] = "ASFADFAFGEC(UUUUUU98U"

@app.route("/")
def base():
    return send_from_directory('../SvelteFrontEnd/public', "index.html")

@app.route("/<path:path>")
def home(path):
    return send_from_directory('../SvelteFrontEnd/public', path)

@app.route("/logIn", methods=["POST"])
def logIn():
    req = request.get_json()
    print(req)
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users WHERE username=:username AND password=:password", {"username": req["username"], "password": req["password"]})
    results = myCursor.fetchall()
    myConnection.close()
    print(results)
    if(len(results) > 0 ):
        loggedIn = "true"
        userType = results[0][2]
    else:
        loggedIn = "false"
        userType = "none"
    res = make_response(jsonify({"loggedIn": loggedIn, "userType": userType}), 200)
    return res

@app.route("/register", methods=["POST"])
def register():
    req = request.get_json()
    print(req)
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users WHERE username=:username", {"username": req["username"]})
    results = myCursor.fetchall()
    myConnection.close()
    print(results)
    if(len(results) == 0 ):

        myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute("""INSERT INTO users (username, password, userType) VALUES(:username, :password, "moderator") """, {"username": req["username"], "password": req["password"]})
        myConnection.commit()
        myConnection.close()



        message = "added new user"


    else:
        message = "A user with this username already exists"
    res = make_response(jsonify({"message": message}), 200)
    return res
@app.route("/getMainPageData", methods=["POST","GET"])
def getMainPageData():
    data = {}

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM news """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    newsArray = []
    for newsItem in result:
        newsArray.append({
            "header": newsItem[0],
            "title": newsItem[1],
            "content": newsItem[2],
            "buttonText": newsItem[3],
        })
    data["news"] = newsArray


    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM sliderItems """)
    result = myCursor.fetchall()
    myConnection.close()
    # slider
    sliderItemsArray = []
    for sliderItem in result:
        sliderItemsArray.append({
            "imageUrl": sliderItem[0],
            "title": sliderItem[1],
            "description": sliderItem[2],
            "interval": sliderItem[3],
        })
    data["sliderItems"] = sliderItemsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM contentCards """)
    result = myCursor.fetchall()
    myConnection.close()
    # contentCards
    contentCardsArray = []
    for contentCard in result:
        contentCardsArray.append({
            "title": contentCard[0],
            "subtitle": contentCard[1],
            "content": contentCard[2],
            "imageURL": contentCard[3],
            "isImageOnLeftSide": True if contentCard[4] == "True" else False,
        })
    data["contentCards"] = contentCardsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM headerItems """)
    result = myCursor.fetchall()
    myConnection.close()
    # header
    headerItemsArray = []
    for headerItem in result:
        headerItemsArray.append({
            "item": headerItem[0],
        })
    data["headerItems"] = headerItemsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM footerItems """)
    result = myCursor.fetchall()
    myConnection.close()
    # footer
    footerItemsArray = []
    for footerItem in result:
        footerItemsArray.append({
            "item": footerItem[0],
        })
    data["footerItems"] = footerItemsArray

    # colors
    selectedThemeId = 0
    with open("../CMSadminapp/config/selectedTheme.txt", "r") as f:
        selectedThemeId = f.read()

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM themes WHERE id = :id """, {"id": selectedThemeId})
    result = myCursor.fetchall()[0]
    myConnection.close()
    colors = {
        "mainBackgroundColor": result[2],
        "secondaryBackgroundColor": result[3],
        "newsHeaderBackgroundColor": result[4],
        "mainTextColor": result[5],
        "secondaryTextColor": result[6]
    }
    data["colors"] = colors
    print(result)
    print(data)

    res = make_response(jsonify(data), 200)
    return res


@app.route("/getEditPageData", methods=["POST","GET"])
def getEditPageData():
    data = {}

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM news """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    newsArray = []
    for newsItem in result:
        newsArray.append({
            "header": newsItem[0],
            "title": newsItem[1],
            "content": newsItem[2],
            "buttonText": newsItem[3],
        })
    data["news"] = newsArray


    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM sliderItems """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    sliderItemsArray = []
    for sliderItem in result:
        sliderItemsArray.append({
            "imageUrl": sliderItem[0],
            "title": sliderItem[1],
            "description": sliderItem[2],
            "interval": sliderItem[3],
        })
    data["sliderItems"] = sliderItemsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM contentCards """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    contentCardsArray = []
    for contentCard in result:
        contentCardsArray.append({
            "title": contentCard[0],
            "subtitle": contentCard[1],
            "content": contentCard[2],
            "imageURL": contentCard[3],
            "isImageOnLeftSide": True if contentCard[4] == "True" else False,
        })
    data["contentCards"] = contentCardsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM headerItems """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    headerItemsArray = []
    for headerItem in result:
        headerItemsArray.append({
            "item": headerItem[0],
        })
    data["headerItems"] = headerItemsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM footerItems """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    footerItemsArray = []
    for footerItem in result:
        footerItemsArray.append({
            "item": footerItem[0],
        })
    data["footerItems"] = footerItemsArray

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM users """)
    result = myCursor.fetchall()
    myConnection.close()
    # news
    usersArray = []
    for user in result:
        usersArray.append({
            "username": user[0],
            "password": user[1],
            "userType": user[2],
        })
    data["users"] = usersArray

    print(data)

    res = make_response(jsonify(data), 200)
    return res


@app.route("/getThemes", methods=["POST","GET"])
def getThemes():
    data = {}

    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM themes ORDER BY id DESC""")
    result = myCursor.fetchall()
    myConnection.close()
    themesArray = []
    for themeItem in result:
        themesArray.append({
            "id": themeItem[0],
            "name": themeItem[1],
            "mainBackgroundColor": themeItem[2],
            "secondaryBackgroundColor": themeItem[3],
            "newsHeaderBackgroundColor": themeItem[4],
            "mainTextColor": themeItem[5],
            "secondaryTextColor": themeItem[6]
        })
    data["themes"] = themesArray

    with open("../CMSadminapp/config/selectedTheme.txt", "r") as f:
        data["selectedThemeId"] = f.read()
    print(data)

    res = make_response(jsonify(data), 200)
    return res


@app.route("/editData", methods=["POST", "GET"])
def editData():
    data = request.get_json()
    # print(data)
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    database = ""
    setValues = ""
    key = ""
    if data["dataType"] == "Users":
        database = "users"
        key = "username"
    elif data["dataType"] == "Nav":
        database = "headerItems"
        key = "item"
    elif data["dataType"] == "Slider":
        database = "sliderItems"
        key = "title"
    elif data["dataType"] == "News":
        database = "news"
        key = "title"
    elif data["dataType"] == "Cards":
        database = "contentCards"
        key = "title"
    elif data["dataType"] == "Footer":
        database = "footerItems"
        key = "item"
    if data["key"] != data["data"][key]:
        myCursor.execute(f"""SELECT * FROM {database} where {key}=:dataKey """, {"dataKey": data["data"][key]})
        result = myCursor.fetchall()
        if len(result) > 0:
            response = make_response(jsonify({"result": "Item already exists", "showError": True}), 418)
            return response
    for updateKey in data["data"]:
        myCursor.execute(f"""UPDATE {database} SET {updateKey}=:updateValue WHERE {key}=:dataKey""", {"dataKey": data["key"], "updateValue": data["data"][updateKey]})
        myConnection.commit()

    myConnection.close()
    return make_response(jsonify({"result": "Item modified"}), 200)


@app.route("/addData", methods=["POST", "GET"])
def addData():
    data = request.get_json()
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    database = ""
    setValues = ""
    setColumns = ""
    key = ""
    if data["dataType"] == "Users":
        database = "users"
        key = "username"
    elif data["dataType"] == "Nav":
        database = "headerItems"
        key = "item"
    elif data["dataType"] == "Slider":
        database = "sliderItems"
        key = "title"
    elif data["dataType"] == "News":
        database = "news"
        key = "title"
    elif data["dataType"] == "Cards":
        database = "contentCards"
        key = "title"
    elif data["dataType"] == "Footer":
        database = "footerItems"
        key = "item"
    myCursor.execute(f"""SELECT * FROM {database} where {key}=:dataKey""", {"dataKey": data["data"][key]})
    result = myCursor.fetchall()
    if len(result) > 0:
        return make_response(jsonify({"result": "Item already exists", "showError": True}), 418)
    queryValues = {}
    for key in data["data"]:
        setColumns += f"""{key},"""
        setValues += f""" :data{key},"""
        queryValues[f"data{key}"] = data["data"][key]
    setColumns = setColumns[0:len(setColumns) - 1]
    setValues = setValues[0:len(setValues)-1]
    myCursor.execute(f"""INSERT INTO {database} ({setColumns}) VALUES ({setValues})""", queryValues)
    myConnection.commit()
    myConnection.close()
    return make_response(jsonify({"result": "Item added"}), 200)


@app.route("/deleteData", methods=["POST", "GET"])
def deleteData():
    data = request.get_json()
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    database = ""
    key = ""
    if data["dataType"] == "Users":
        database = "users"
        key = "username"
    elif data["dataType"] == "Nav":
        database = "headerItems"
        key = "item"
    elif data["dataType"] == "Slider":
        database = "sliderItems"
        key = "title"
    elif data["dataType"] == "News":
        database = "news"
        key = "title"
    elif data["dataType"] == "Cards":
        database = "contentCards"
        key = "title"
    elif data["dataType"] == "Footer":
        database = "footerItems"
        key = "item"
    myCursor.execute(f"""DELETE FROM {database} where {key}=:dataKey""", {"dataKey": data["key"]})
    myConnection.commit()
    myConnection.close()
    return make_response(jsonify({"result": "Item deleted"}), 200)


@app.route("/addTheme", methods=["POST", "GET"])
def addTheme():
    data = request.get_json()
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("INSERT INTO themes (name, mainBackgroundColor, secondaryBackgroundColor, newsHeaderBackgroundColor, mainTextColor, secondaryTextColor) VALUES (:name, :mainBackgroundColor, :secondaryBackgroundColor, :newsHeaderBackgroundColor, :mainTextColor, :secondaryTextColor)", {"name": data["name"], "mainBackgroundColor": data["mainBackgroundColor"], "secondaryBackgroundColor": data["secondaryBackgroundColor"], "newsHeaderBackgroundColor": data["newsHeaderBackgroundColor"], "mainTextColor": data["mainTextColor"], "secondaryTextColor": data["secondaryTextColor"]})
    myConnection.commit()
    myConnection.close()
    return make_response(jsonify({"result": "Theme added"}), 200)

@app.route("/selectTheme", methods=["POST", "GET"])
def selectTheme():
    data = request.get_json()
    print(data)
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("UPDATE themes SET mainBackgroundColor = :mainBackgroundColor, secondaryBackgroundColor = :secondaryBackgroundColor, newsHeaderBackgroundColor = :newsHeaderBackgroundColor, mainTextColor = :mainTextColor, secondaryTextColor = :secondaryTextColor WHERE id = :id ", {"id": data["selectedThemeId"],  "mainBackgroundColor": data["mainBackgroundColor"], "secondaryBackgroundColor": data["secondaryBackgroundColor"], "newsHeaderBackgroundColor": data["newsHeaderBackgroundColor"], "mainTextColor": data["mainTextColor"], "secondaryTextColor": data["secondaryTextColor"]})
    myConnection.commit()
    myConnection.close()
    with open("../CMSadminapp/config/selectedTheme.txt", "w") as f:
        f.write(str(data["selectedThemeId"]))
    return make_response(jsonify({"result": "Theme selected"}), 200)
@app.route("/getComments", methods=["POST", "GET"])
def getComments():
    # { articleId: 1 }
    data = request.get_json()
    output = {}
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM comments WHERE articleId = :articleId ", {"articleId": data["articleId"]})
    comments = myCursor.fetchall()
    myConnection.close()

    commentsArray = []
    for comment in comments:
        commentsArray.append({
            "articleId": comment[0],
            "author": comment[1],
            "date": comment[2],
            "content": comment[3]
        })
    output["comments"] = commentsArray

    return make_response(jsonify(output), 200)
@app.route("/addComment", methods=["POST", "GET"])
def addComment():
    # { articleId: 1, author: sss, date: sss, content: sss }
    data = request.get_json()
    output = {}
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute("INSERT INTO comments (articleId, author, date, content) VALUES (:articleId, :author, :date, :content) ",
                     {
                         "articleId": data["articleId"],
                         "author": data["author"],
                         "date": data["date"],
                         "content": data["content"]
                     })
    myConnection.commit()
    myConnection.close()
    output["message"] = "added comment successfully"
    return make_response(jsonify(output), 200)
if __name__ == "__main__":
    app.run(debug=True)