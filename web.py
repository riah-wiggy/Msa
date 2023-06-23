import flask

app= flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def index():
    return "<h1 style='color:green'> My name is Riah</h1>"
app.run()