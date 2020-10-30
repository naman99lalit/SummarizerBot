import requests as _req
from bs4 import BeautifulSoup as bs
from summarizer import FrequencySummarizer as fs


# Text summarizer call
def summ_from_text(text):
    n=2
    summary = fs().summarize(text,n)
    print("summary")
    print (summary) 
    return ' '.join(summary)


# URL Func 
def shorten_news(url, n = 4):
    print("inside get_news of shorten_news")
    response = _req.get(url)
    print(response)
    if not response.ok:
        return False
    page = response.content
    soup = bs(page, "lxml")
    print("soup")
    summary = fs().summarize("\n".join([x.text for x in soup.findAll("p") if len(x.text.split()) > 1]), n)
    print("summary")
    print(summary) 
    summary.insert(0, soup.title.text)
    print("nxjnd")
    return ' '.join(summary)