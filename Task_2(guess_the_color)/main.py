from flask import Flask, render_template, request, jsonify
import sqlite3
from random import randint


app = Flask(__name__)


def db_create():
    with sqlite3.connect("Objects.db") as c:
        c.cursor().execute(f'DROP TABLE IF EXISTS Objects;')
        c.cursor().execute(f'CREATE TABLE Objects (id INTEGER PRIMARY KEY AUTOINCREMENT, color text);')

    def add_to_db(color):
        with sqlite3.connect("Objects.db") as c:
            c.cursor().execute(f'INSERT INTO Objects (color) VALUES (\'{color}\')')

    Objects = []
    for i in range(1, 101):
        if i <= 60:
            Objects.append("Blue")
        elif i <= 80:
            Objects.append("Green")
        else:
            Objects.append("Red")

    for i in range(len(Objects)):
        r = randint(0, len(Objects) - 1)
        add_to_db(Objects[r])
        print(Objects[r], r, len(Objects))
        Objects.pop(r)


def find(object_id):
    with sqlite3.connect("Objects.db") as c:
        return c.cursor().execute(f"select color from Objects where id = '{object_id}'").fetchone()[0]


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        try:
            print(request.form)
            object_id = request.form.get("id")
            return jsonify(find(object_id))
        except:
            return jsonify(False)


db_create()


app.run(host="localhost")

