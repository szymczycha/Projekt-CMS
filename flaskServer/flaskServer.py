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
    myCursor.execute(f"""SELECT * FROM users WHERE username="{req["username"]}" AND password="{req["password"]}" """)
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
    myCursor.execute(f"""SELECT * FROM users WHERE username="{req["username"]}" """)
    results = myCursor.fetchall()
    myConnection.close()
    print(results)
    if(len(results) == 0 ):

        myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
        myCursor = myConnection.cursor()
        myCursor.execute(f"""INSERT INTO users (username, password, userType) VALUES("{req["username"]}", "{req["password"]}", "moderator") """)
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
    myCursor.execute(f"""SELECT * FROM themes """)
    result = myCursor.fetchall()
    myConnection.close()
    themesArray = []
    for themeItem in result:
        themesArray.append({
            "id": themeItem[0],
            "mainBackgroundColor": themeItem[1],
            "secondaryBackgroundColor": themeItem[2],
            "newsHeaderBackgroundColor": themeItem[3],
            "mainTextColor": themeItem[4],
            "secondaryTextColor": themeItem[5]
        })
    data["themes"] = themesArray

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
    myCursor.execute(f"""SELECT * FROM {database} where {key}="{data["data"][key]}" """)
    result = myCursor.fetchall()
    if len(result) > 0:
        response = make_response(jsonify({"result": "Item already exists"}), 418)
        return response
    for key in data["data"]:
        setValues += f""" {key}='{data["data"][key]}',"""
    setValues = setValues[0:len(setValues)-1]
    print(setValues[0:len(setValues)-2])
    print(f"""UPDATE {database} SET{setValues} WHERE {key}="{data["key"]}" """)
    myCursor.execute(f"""UPDATE {database} SET{setValues} WHERE {key}="{data["key"]}" """)
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
    myCursor.execute(f"""SELECT * FROM {database} where {key}="{data["data"][key]}" """)
    result = myCursor.fetchall()
    if len(result) > 0:
        return make_response(jsonify({"result": "Item already exists"}), 418)
    for key in data["data"]:
        setColumns += f"""{key},"""
        setValues += f""" "{data["data"][key]}","""
    setColumns = setColumns[0:len(setColumns) - 1]
    setValues = setValues[0:len(setValues)-1]
    myCursor.execute(f"""INSERT INTO {database} ({setColumns}) VALUES ({setValues}) """)
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
    myCursor.execute(f"""DELETE FROM {database} where {key}="{data["key"]}" """)
    myConnection.commit()
    myConnection.close()
    return make_response(jsonify({"result": "Item deleted"}), 200)

if __name__ == "__main__":
    app.run(debug=True)