from flask import  Flask,render_template, url_for

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")
@app.route("/bestsel")
def bestseller():
    return render_template("bestseller.html")
@app.route("/categories")
def categories():
    return render_template("categories.html")
@app.route("/writers")
def writers():
    return render_template("writers.html")


app.run(debug=True)