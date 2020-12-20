# Example of response object can be found here:
# https://dev.tisane.ai/docs/services/5a3b6668a3511b11cc292655/operations/5a3b7177a3511b11cc29265c
from InnoGuard import Constants
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64


def analyse_text(text_for_analysis):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': Constants.TISANE_API_KEY_1,
    }

    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('api.tisane.ai')
        conn.request("POST", "/parse?%s" % params, text_for_analysis, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
