# -------------------------------------------------------------------------------
# Flow orchestration process
# -------------------------------------------------------------------------------
import csv
import dataanalysis.requestanalysis as ra
import totalvirusapi.apicall as api_call
from configuration.config import API_KEY

def run():
    #Initialize objects
    try:
        apicall = api_call.ToatlVirusAPI(API_KEY) # API call to TotalVirus
        req = ra.RequestProcess() # API response processing

        # open file with a list of sites and start processing
        with open('data/request1.csv', newline='') as read_obj:
            csv_reader = csv.reader(read_obj)
            urls = list(csv_reader)
            for url in urls:
                response = apicall.get_report(url)
                req.get_analysis_results(response)
                req.output_analysis('print')
    except Exception as e:
        print(e)


