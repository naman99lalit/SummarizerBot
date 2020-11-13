from flask import Flask, render_template, send_from_directory, request
from internet_conn import summ_from_text, shorten_news
from flask_restful import Api, Resource, reqparse
from query import QueryService

app = Flask(__name__)
api = Api(app)
api.add_resource(QueryService, '/news_urls')

# Introduction
@app.route("/")
def index():
    return render_template("index.html")


# Text conversion
@app.route("/text_con", methods = ["POST", "GET"])
def text_con():
    return render_template("inputtext.html")


# URL conversion
@app.route("/url_con", methods = ["POST", "GET"])
def url_con():
    return render_template("url.html")



# Speech Input - Route
@app.route("/speech_con", methods = ["POST", "GET"])
def speech_con():
    print("Inside Speech route")
    return render_template("speech_inpt.html")


# Text Input Results
@app.route("/results",methods=["POST"])
def result():
    print("inside app index")
    text = request.form['input_text']
    print(text)
    var = summ_from_text(text)
    print("var")
    print(var)
    return render_template("inputtext.html", output_summary = var)


# URL Input Results
@app.route("/url_results",methods=["POST"])
def url_result():
    print("inside url func")
    url = request.form['input_text']
    print(url)
    result = shorten_news(url)
    print("result")
    print(result)
    return render_template("url.html",output_summary=result)



if __name__ == '__main__':
    try:
        app.run('localhost', port = 3000, debug=True, use_reloader = False)
    except(Exception, e):
        print(e)

