from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
port = os.environ.get("PORT", 5000)

@app.route("/", methods=['GET','POST'])
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)

@app.route("/projects")
def projects():
    title = "Projects"
    return render_template("projects.html", title=title)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=port)