import re
import json
from flask import request
import facebook
import requests
import csv
import numpy as np
import sys
import pandas as pd
import environment as env

from app import app

@app.route("/getfacebook", methods=["GET", "POST"])

def getRatings():
    # Authentication
    ACCESS_TOKEN = env.FACEBOOK_API_KEY
    # GET requests in FB me?fields=ratings
    URL = f"https://graph.facebook.com/v8.0/me?fields=ratings&access_token={ACCESS_TOKEN}"


    data = []
    r = requests.get(URL)  # Make a GET request to the given URL
    data.append(r.json())  # Extract data in the json form and append it into the list named "data"
    count = pos = neg = neut = 0

    if 'Error' in data[0].keys() or 'error' in data[0].keys():
        print('Error Occured!')
        print(data[0]['error']['message'])
        sys.exit(0)
    try:    
        with open('FBdata.csv', mode='w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['created_time', 'recommendation_type', 'review_text'])
            for i in data[0]['ratings']['data']:
                writer.writerow([i['created_time'], i['recommendation_type'], i['review_text']])
                if i['recommendation_type'] == "positive":
                    pos +=1
                if i['recommendation_type'] == "negative":
                    neg +=1
                if i['recommendation_type'] == "neutral":
                    neut +=1
                count +=1               

                print(count, pos, neg, neut,[i['created_time'], i['recommendation_type'], i['review_text']])
            sentiment = [neg, neut, pos]


    except Exception as e:
        print('Error in writing...')
        print(e)


    return json.dumps({"message": "data has been saved", "result_list": sentiment, "all_data": data[0]['ratings']['data']})
