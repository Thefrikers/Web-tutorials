from flask import Flask,render_template,url_for
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('Signup//Signin.html')

@app.route("/index2")
def index2():
    return render_template('Index.html')


