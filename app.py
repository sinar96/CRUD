from flask import Flask, render_template, redirect, session, request
import datetime
from db import database
from models import Lists

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)

# Mainpage
@app.route("/")
def home():
    return render_template("index.html", **locals())

# show all list
@app.route("/lists")
def alllists():
    # Lists.query.all() == select*from lists(tablename)
    lists = Lists.query.all()
    return render_template("lists.html",  **locals())

# create list
@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        name = request.form.get("name", None)
        age = request.form.get("umur", None)
        # create new record in database
        lists =Lists(name,age)
        database.session.add(lists)
        database.session.commit()
        return redirect("/lists")

    return render_template("add.html", **locals())


if __name__=="__main__":
	app.run(debug=True)
