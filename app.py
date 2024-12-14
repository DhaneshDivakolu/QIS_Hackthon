from flask import Flask,render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/marchent", methods = ["GET"])
def home():
    return render_template("marchent.html")

@app.route("/user", methods = ["GET"])
def home():
    return render_template("user.html")

@app.route("/management", methods = ["GET"])
def management():
    return render_template("management.html")

@app.route("/m_register", methods = ["GET"])
def m_register():
    return render_template("m_register.html")

@app.route("/m_login", methods = ["GET"])
def m_login():
    return render_template("m_login.html")

@app.route("/u_register", methods = ["GET"])
def u_register():
    return render_template("u_register.html")

@app.route("/u_login", methods = ["GET"])
def u_login():
    return render_template("u_login.html")

