### URL: https://languagetool.org/http-api/

from pprint import pprint
import requests
import json

endpoint = "https://api.languagetool.org/v2/check"

data = {
    "text": "Be like water, it go where it want, not where you force it go. You must learning to adapt fast and no resist changes.",
    "language": "auto"
}

response = requests.post(endpoint, data=data)
data = json.loads(response.text)
pprint(data)