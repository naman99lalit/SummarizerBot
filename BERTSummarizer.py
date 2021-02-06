import requests

def bertSummariser(text_body, number_of_sentences):


    body = text_body
    url = "https://api.smrzr.io/v1/summarize?num_sentences=" + str(number_of_sentences) + "&algorithm=kmeans&min_length=40&max_length=500"
    resp = requests.post(
        url, 
        data=body
    )
    return resp.json()["summary"]

def bertSummariserNews(page_url, number_of_sentences):

    json_body = {
        "url": page_url
    }

    url = "https://api.smrzr.io/v1/summarize/news?num_sentences=" + str(number_of_sentences) + "&min_length=40"

    resp = requests.post(url, json=json_body).json()
    summary = resp['summary']
    return summary
