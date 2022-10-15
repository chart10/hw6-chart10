# Christian Hart 001-68-3628

import flask
from googlebooks import get_books

API_KEY = "AIzaSyB9rj90xdvrcoqC3HrAc1kZME83TX_P2Fk"

app = flask.Flask(__name__)

books = ["The+Stranger", "Dune", "The+Bell+Jar",
         "House of Leaves", "A Scanner Darkly", "Zorba the Greek"]
covers = ["https://i.guim.co.uk/img/media/650851a40923295ad181cbf199e4e1ffdf1b3cfb/0_0_800_1322/master/800.jpg?width=700&quality=85&auto=format&fit=max&s=d418e1d020be3746920996d08a0be5dd",
          "https://i.pinimg.com/474x/87/06/1b/87061b3f7604fe7a5ac38b28c6b64430.jpg",
          "http://prodimage.images-bn.com/pimages/9780060837020_p0_v1_s1200x630.jpg",
          "https://horrornovelreviews.files.wordpress.com/2014/11/dscn6768_3.jpg",
          "https://schicksalgemeinschaft.files.wordpress.com/2021/06/a-scanner-darkly-pepper.jpg",
          "https://pictures.abebooks.com/inventory/30789968188.jpg"]


@app.route("/")
def index():

    dynoBooks = []
    dynoCovers = []
    i = 0
    for book in books:
        entry = get_books(book)
        dynoBooks.append(entry[0])
        dynoCovers.append(entry[1])
        i += 1

    print(dynoBooks)
    print(dynoCovers)
    return flask.render_template(
        "index.html",
        dynoBooks=dynoBooks,
        len=len(dynoBooks),
        dynoCovers=dynoCovers
    )


app.run(debug=True)
