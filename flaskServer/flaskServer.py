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

if __name__ == "__main__":
    app.run(debug=True)