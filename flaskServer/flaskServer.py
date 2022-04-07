from flask import Flask, render_template, request, jsonify, make_response
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired
from math import pi
import sqlite3


app = Flask(__name__)
app.config["SECRET_KEY"] = "ASFADFAFGEC(UUUUUU98U"
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/logIn", methods=["POST"])
def logIn():
    req = request.get_json()
    print(req)
    myConnection = sqlite3.connect('../CMSadminapp/CMS.db')
    myCursor = myConnection.cursor()
    myCursor.execute(f"""SELECT * FROM users WHERE username={req.username} AND password={req.password}""")
    results = myCursor.fetchall()
    myConnection.close()
    print(results)
    message = "ok" if len(results) > 0 else "nieok"
    res = make_response(jsonify({"message": message}), 200)
    return res
if __name__ == "__main__":
    app.run(debug=True)