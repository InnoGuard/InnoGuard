# Example of response object can be found here:
# https://dev.tisane.ai/docs/services/5a3b6668a3511b11cc292655/operations/5a3b7177a3511b11cc29265c
# from scripts import Constants
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json

import libs.Constants


def analyse_text(text_for_analysis):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': libs.Constants.TISANE_API_KEY_1,
    }
    body = {
        "language": "en",
        "content": text_for_analysis,
        "settings": {}
    }
    params = urllib.parse.urlencode({
    })
    conn = http.client.HTTPSConnection('api.tisane.ai')
    conn.request("POST", "/parse?%s" %
                 params, json.dumps(body), headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    return data


r = analyse_text("Test String Goes Here")
print(r)