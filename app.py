# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:05:17 2024

@author: jenul
"""
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extracting some data from the webpage
    data = {'title': soup.title.string}
    # You can add more scraping logic here using BeautifulSoup

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:05:17 2024

@author: jenul
"""

