from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summary_from_text(data):
    
    doc = str(data)
    
    parser=PlaintextParser.from_string(doc,Tokenizer("english"))
    # Using LexRank
    summarizer = LexRankSummarizer()
    #Summarize the document with 4 sentences
    summary = summarizer(parser.document,4)
    # for sentence in summary:
    #     print(sentence)
    
    return summary