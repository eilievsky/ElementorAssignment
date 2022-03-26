# -------------------------------------------------------------------------------
# Model for class definition of request analysis
# -------------------------------------------------------------------------------

from collections import Counter
from configuration.config import NOT_SAFE_KEYWORDS
import datetime as dt

class RequestProcess():
    def __init__(self ):
        self.analysis_res = {}

    # ----- Request analaysis process function
    def get_analysis_results(self,req_response):

        self.req_response = req_response
        self.analysis_res['url'] = self.req_response["data"]["attributes"]["url"]
        self.analysis_res['last_modification_date'] = self.req_response["data"]["attributes"]["last_modification_date"]

        # calculate voting
        voting_list = []
        for el, voting in self.req_response["data"]["attributes"]["last_analysis_results"].items():
            voting_list.append(voting["result"])

        # check if site at risk or safe
        if set(NOT_SAFE_KEYWORDS).isdisjoint(voting_list):
            self.analysis_res['site_risk'] = 'safe'
        else:
            self.analysis_res['site_risk'] = 'risk'

        #summarize voting values
        voting_dict = Counter(voting_list)
        self.analysis_res['voting_analysis'] = dict(voting_dict)

        # Calculate categories
        cat_dict = self.req_response["data"]["attributes"]["categories"]
        # summarize category values
        cat_dict_summary = Counter(cat_dict.values())
        self.analysis_res['category_analysis'] = dict(cat_dict_summary)

        return self.analysis_res

    # ---- out analysis results
    # since analysis is stored in data dictionary it can be processed different. Current implementation contains only standard output
    def output_analysis(self, output_type):
        # This function should provide different output types
        if output_type == "print":
            print(f"URL: {self.analysis_res['url']}")
            print(f"Last modification time: {dt.datetime.fromtimestamp(self.analysis_res['last_modification_date'])} ")
            print(f"Site risk: {self.analysis_res['site_risk']}")
            print(f"Voting Analysis: {self.analysis_res['voting_analysis']}")
            print(f"Category Analysis: {self.analysis_res['category_analysis']}")

        elif output_type == "db":
            pass
        else:
            pass






