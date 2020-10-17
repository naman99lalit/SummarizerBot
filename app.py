from flask import Flask, render_template, send_from_directory, request
from internet_conn import summ_from_text

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/text_con", methods = ["POST", "GET"])
def text_con():
    return render_template("inputtext.html")


@app.route("/results",methods=["POST"])
def result():
    print("inside app index")
    text = request.form['input_text']
    print(text)
    var = summ_from_text(text)
    print("var")
    print(var)
    return render_template("inputtext.html", output_summary = var)


if __name__ == '__main__':
    try:
        app.run('localhost', port = 3000, debug=True, use_reloader = False)
    except(Exception, e):
        print(e)

