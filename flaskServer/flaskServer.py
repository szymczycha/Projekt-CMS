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
if __name__ == "__main__":
    app.run(debug=True)