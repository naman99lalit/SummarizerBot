from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summary_from_lex_text(data, length):
    
    doc = str(data)

    length = int(length)
    
    parser=PlaintextParser.from_string(doc,Tokenizer("english"))
    # Using LexRank
    summarizer = LexRankSummarizer()
    #Summarize the document with 5 sentences
    summary = summarizer(parser.document,length)
    # for sentence in summary:
    #     print(sentence)
    
    return summary