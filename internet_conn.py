from summarizer import FrequencySummarizer as fs



def summ_from_text(text):
    n=2
    summary = fs().summarize(text,n)
    print("summary")
    print (summary) 
    return ' '.join(summary)