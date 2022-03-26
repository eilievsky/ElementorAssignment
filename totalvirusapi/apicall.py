# -------------------------------------------------------------------------------
# Model for class definition of Total Virus requestpip
# -------------------------------------------------------------------------------

import base64
import requests

class ToatlVirusAPI():
    def __init__(self, api_key):
        self.api_key = api_key

    def get_report(self , examine_url):
        url_id = base64.urlsafe_b64encode(examine_url[0].encode()).decode().strip("=")
        url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        header = {
            "Accept": "application/json",
            "X-Apikey": self.api_key
        }

        response = requests.request("GET", url, headers=header)
        self.response = response

        return response.json()
