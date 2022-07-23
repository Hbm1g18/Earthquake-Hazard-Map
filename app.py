from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'coilline8'

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

