# Christian Hart 001-68-3628

import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


app.run()
