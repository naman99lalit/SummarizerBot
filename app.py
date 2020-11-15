from flask import Flask, render_template, send_from_directory, request
from internet_conn import summ_from_text, shorten_news, shorten_lex_text
from flask_restful import Api, Resource, reqparse
from query import QueryService
from LexRankSummarizer import summary_from_text

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
    text = request.form['input_text']
    print(text)
    
    # Algo 1 (Word Frequency)
    algo1_summ = summ_from_text(text)
    print("TF Summary: ", algo1_summ)

    # Algo 2 (LexRank Algo)
    result = summary_from_text(text)
    
    algo2_sum = ""
    for i in range(len(result)):
        algo2_sum += str(result[i])

    print("LexRank Summary: ", algo2_sum)


    return render_template("inputtext.html", output_summary1 = algo1_summ, output_summary2 = algo2_sum)


# URL Input Results
@app.route("/url_results",methods=["POST"])
def url_result():
    print("inside url func")
    url = request.form['input_text']
    print(url)
    
    # Word Freq Algorithm 
    wf_result = shorten_news(url)
    print("wf_result: ", wf_result)

    # LexRank Algorithm
    lr_result = shorten_lex_text(url)
    print("lr_result: ", lr_result)

    return render_template("url.html",output_summary1 = wf_result, output_summary2 = lr_result)



if __name__ == '__main__':
    try:
        app.run('localhost', port = 3000, debug=True, use_reloader = False)
    except(Exception, e):
        print(e)

