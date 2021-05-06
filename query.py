
import os
import sys
sys.path.insert(0,os.path.abspath('..'))
import internet_conn
from json import loads as _l
import query_extractor as _qe
from flask_restful import Resource, reqparse
from internet_conn import (shorten_news, get_gkg, GuardianAggregator as _ga, NYTAggregator as _nyt)


class QueryService(Resource):
    def post(self):
        # print("inside QueryService")
        args = parser.parse_args()
        # print("args",args)
        result = clf.predict(args["data"])
        # print("result",result)
        return result[0], 200 if result[1] else 400


class QueryAnalyzer(object):
    def __init__(self):
        # print("inside QueryAnalyzer")
        self._query_extractor = _qe.QueryExtractor()

    def predict(self, data):
        # print("inside predict")
        try:
            if "news" in data.lower() or "latest" in data.lower():
                # News query
                # print("inside news")
                source, query = self._query_extractor.get_news_tokens(data)
                response = (_ga() if "guardian" in source else _nyt()).get_news(query)
                # print("Printing response")
                # print(response)
                if len(response) <= 0:
                    return {"phrase": "Sorry, no relevant results were returned."}, 500
                i, done = 0, internet_conn.shorten_news(response[0])
                while (not done) and ((i + 1) < len(response)):
                    i += 1
                   # print response[i]
                    done = shorten_news(response[i])

            else:
                # Knowledge query
                done = get_gkg(self._query_extractor.get_knowledge_tokens(data))
            # print("done is below")
            # print(done)
            ret_val = {"urls": done}
            if not done:
                ret_val["phrase"] = "Sorry, no valid results were returned."
            return ret_val, done
        except (Exception, e):
            return {"phrase": "Sorry, something wrong happened.", "original_exception": e.message}, False


parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()
