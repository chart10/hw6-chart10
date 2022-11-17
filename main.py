# Christian Hart 001-68-3628

import flask
import os
from flask_sqlalchemy import SQLAlchemy
from requests import request
from googlebooks import get_books, get_first_five

API_KEY = "AIzaSyB9rj90xdvrcoqC3HrAc1kZME83TX_P2Fk"

app = flask.Flask(__name__)

# TODO: Insert SQLAlchemy boiler plate code
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "database.db")
db = SQLAlchemy(app)

# TODO: Design database structure for FavoritesList:
# Columns: ID(primary-key), title, subtitle, author, thumbnail


class FavList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    subtitle = db.Column(db.String(80))
    author = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))


with app.app_context():
    db.create_all()


# Hardcoded favorites list
books = ["The Stranger", "Dune", "The Bell Jar",
         "House of Leaves", "A Scanner Darkly", "Zorba the Greek"]
covers = ["https://i.guim.co.uk/img/media/650851a40923295ad181cbf199e4e1ffdf1b3cfb/0_0_800_1322/master/800.jpg?width=700&quality=85&auto=format&fit=max&s=d418e1d020be3746920996d08a0be5dd",
          "https://i.pinimg.com/474x/87/06/1b/87061b3f7604fe7a5ac38b28c6b64430.jpg",
          "http://prodimage.images-bn.com/pimages/9780060837020_p0_v1_s1200x630.jpg",
          "https://horrornovelreviews.files.wordpress.com/2014/11/dscn6768_3.jpg",
          "https://schicksalgemeinschaft.files.wordpress.com/2021/06/a-scanner-darkly-pepper.jpg",
          "https://pictures.abebooks.com/inventory/30789968188.jpg"]


# add app.route() for this process
# Generate new HTML form for each API query result (hidden inputs for
#   each db field)
# new route should redirect to mainpage when finished adding
# Auto add my entries to the database
# TODO: Allow user to remove entries from the database
# add app.route() for favorite deletion
# create HTML form for each favorite (button which starts
#   deletion process)


@app.route("/", methods=["GET", "POST"])
def index():

    # TODO: Allow user to add entries to the database
    if flask.request.method == "POST":
        data = flask.request.form
        new_fav = FavList(
            title=data["title"],
            subtitle=data["subtitle"],
            author=data["author"],
            thumbnail=data["thumbnail"],
        )

    # dynoBooks = []
    # dynoCovers = []
    # i = 0
    # for book in books:
    #     entry = get_books(book)
    #     dynoBooks.append(entry[0])
    #     dynoCovers.append(entry[1])
    #     i += 1

    # if flask.request.args.get('search') == None:

    searchvalue = flask.request.args.get('search')
    userresults = []
    if searchvalue != None:
        userresults = (get_first_five(searchvalue))

    return flask.render_template(
        "index.html",
        # dynoBooks=dynoBooks,
        len=len(books),
        # dynoCovers=dynoCovers,
        books=books,
        covers=covers,
        searchvalue=searchvalue,
        userresults=userresults
    )


app.run(debug=True)
