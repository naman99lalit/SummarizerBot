from flask import Flask, render_template, send_from_directory, request
from internet_conn import summ_from_text, shorten_news, shorten_lex_text
from flask_restful import Api, Resource, reqparse
from query import QueryService
from LexRankSummarizer import summary_from_lex_text
from audio_conversion import convert_mp3_to_wav, convert_audio_to_text

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


# Audio File as Input - Route
@app.route("/speech_aud", methods = ["POST", "GET"])
def speech_aud():
    print("Inside Speech route where audio file as input")
    return render_template("speech_aud.html")


# Audio Input Results
@app.route("/speech_results",methods=["POST"])
def speech_result():
    audio_file = request.form['input_file']
    print(type(audio_file))

    converted_audio_file = convert_mp3_to_wav(audio_file)

    text = convert_audio_to_text(converted_audio_file)
    
    # Algo 1 (Word Frequency)
    algo1_summ = summ_from_text(text, 5)
    print("TF Summary: ", algo1_summ)

    # Algo 2 (LexRank Algo)
    result = summary_from_lex_text(text, 5)
    
    algo2_sum = ""
    for i in range(len(result)):
        algo2_sum += str(result[i])

    print("LexRank Summary: ", algo2_sum)


    return render_template("speech_aud.html", output_summary1 = algo1_summ, output_summary2 = algo2_sum)



# Text Input Results
@app.route("/results",methods=["POST"])
def result():
    text = request.form['input_text']
    length = request.form['input_sentence']
    print(text, length)
    
    # Algo 1 (Word Frequency)
    algo1_summ = summ_from_text(text, length)
    print("TF Summary: ", algo1_summ)

    # Algo 2 (LexRank Algo)
    result = summary_from_lex_text(text, length)
    
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
    length = request.form['input_sentence']
    print(url, length)
    
    # Word Freq Algorithm 
    wf_result = shorten_news(url, length)
    print("wf_result: ", wf_result)

    # LexRank Algorithm
    lr_result = shorten_lex_text(url, length)
    print("lr_result: ", lr_result)

    algo2_sum = ""
    for i in range(len(lr_result)):
        algo2_sum += str(lr_result[i])

    return render_template("url.html",output_summary1 = wf_result, output_summary2 = algo2_sum)



if __name__ == '__main__':
    try:
        app.run('localhost', port = 3000, debug=True, use_reloader = False)
    except(Exception, e):
        print(e)

