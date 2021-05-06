from summa.summarizer import summarize

def textRankSummarizer(text, sentence_length):
    result = summarize(text, ratio = 1.0)
    text_len = result.count('.')
    lst = result.split('.')
    return (".".join(lst[:min(int(sentence_length), int(text_len))]))
