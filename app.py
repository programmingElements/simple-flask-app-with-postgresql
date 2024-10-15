from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__, template_folder='templates')

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@dev-postgres:5432/books"
db = SQLAlchemy(app)
background_color = os.environ.get('BACKGROUND_COLOR');

# Books Database Example CRUD Operations 

from models import Book

@app.route('/')
def index():
  mylist = [10, 20, 30, 40, 50]
  return render_template('index.html', color=background_color, mylist=mylist)

@app.route('/home')
def home():
  some_text = "Hello World!"
  books = Book.query.all()
  return render_template('home.html', some_text=some_text, books=books)

@app.route("/create", methods=["POST"])
def create():
    book = Book(title=request.form.get("title"))
    db.session.add(book)
    db.session.commit()
    return redirect("/")

@app.route("/update", methods=["POST"])
def update():
    title = request.form.get("title")
    return render_template("update_book.html", title=title)

@app.route("/update-title", methods=["POST"])
def update_title():
    old_title = request.form.get("old_title")
    new_title = request.form.get("new_title")
    book = Book.query.filter_by(title=old_title).first()
    book.title = new_title
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")



@app.template_filter('reverse_string')
def reverse_string(s):
  return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=2):
  return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
  return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

@app.route('/redirect_endpoint')
def redirect_endpoint():
  return redirect(url_for('home'))


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5001, debug=True)