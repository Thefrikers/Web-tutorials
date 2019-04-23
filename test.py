from flask import Flask,render_template,url_for
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('Signup//Signin.html')

@app.route("/index2")
def index2():
    return render_template('Index.html')

@app.route("/signup")
def signup():
    return render_template('Signup//signup.html')

@app.route("/editor")
def editor():
    return render_template('Topics//Editor.html')

@app.route("/attributes")
def attributes():
    return render_template('Topics//Attributes.html')

@app.route("/basics")
def basics():
    return render_template('Topics//Basics.html')

@app.route("/blocks")
def blocks():
    return render_template('Topics//Blocks.html')

@app.route("/colors")
def colors():
    return render_template('Topics//COLORS.html')

@app.route("/comments")
def comments():
    return render_template('Topics//Comments.html')

@app.route("/contact")
def contact():
    return render_template('Topics//Contact.html')

@app.route("/elements")
def elements():
    return render_template('Topics//Elements.html')

@app.route("/formatting")
def formatting():
    return render_template('Topics//Formatting.html')

@app.route("/headings")
def headings():
    return render_template('Topics//Headings.html')

@app.route("/ids")
def ids():
    return render_template('Topics//Id.html')

@app.route("/iframe")
def iframe():
    return render_template('Topics//Iframe.html')

@app.route("/intro")
def intro():
    return render_template('Topics//Intro.html')

@app.route("/paragraphs")
def paragraphs():
    return render_template('Topics//paragraphs.html')

@app.route("/quations")
def quations():
    return render_template('Topics//Quatation.html')

@app.route("/style")
def style():
    return render_template('Topics//Style.html')

@app.route("/videos")
def videos():
    return render_template('Topics//Videos.html')

@app.route("/main")
def main():
    return render_template('Main.html')
