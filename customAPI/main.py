from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  """
  Fetch currency rate from X-Rates website for specified currencies.
  """

  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate
  

app = Flask(__name__)

@app.route("/")
def hello():
    """
    Simple home page.
    """
    return "<h1>Current Rate API</h1><p>Example URL: /api/v1/usd-eur</p>"


@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  """
  Return JSON API object with currency rate date.

  Example: 
      {"input_currency":"usd","output_currency":"eur","rate":0.859388}
  """
  rate = get_currency(in_cur, out_cur)
  result_dictionary = {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
  
  # Convert to JSON format.
  return jsonify(result_dictionary)

app.run(host="localhost", port=5000)