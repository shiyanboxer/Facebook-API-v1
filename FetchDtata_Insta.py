import requests
# from json import dump
# import time
import csv
import sys

ACCESS_TOKEN = 'EAAK0u28Gh14BAGzjGnxXgcpgXvrdJeq4ks4BAVZApBSXvm99TGvihkhuZB5BHbguUx2PnBkvinWXyhUj8hvnDvZACJQzS1oRzZBc9bglXjQ4yrOW80vXA0ecbm0Gb6YuvllwwNm32S6jVzHnZCXTN2JIAhEZAFZBNpwgTcXIZCRw2xiRuoFRE9MJ8TQZBEnlcBZBSZBbX3MzZCKmggZDZD'
data = []

# RECENT

URL = f'https://graph.facebook.com/v8.0/me?fields=id,name,about,category,emails,engagement,country_page_likes,fan_count,link,talking_about_count,blocked{​username}​,likes.limit(5),rating_count,ratings.limit(5),posts.limit(5),visitor_posts.limit(5),tagged.limit(5)&access_token={ACCESS_TOKEN}'


r = requests.get(URL)  # Make a GET request to the given URL
data.append(r.json())  # Extract data in the json form and append it into the list named "data"

if 'Error' in data[0].keys() or 'error' in data[0].keys() :
    print('Error Occured!')
    print(data[0]['error']['message'])
    sys.exit(0)


# Make request for 50 times and made above one request so total 51 requests
for i in range(50):
    try:
        # time.sleep(1) # to give delay of 1 sec.
        # print(i+1) # to know something is happening
        temp_url = data[0]['paging']['next']  # extract linnk of next page
        temp_data = requests.get(temp_url).json() # get data of the page and again append into the list name "data"
        # print(temp_data.keys())
        if 'Error' in data[0].keys() or 'error' in data[0].keys():
            print('Error')
            break
        data.append(temp_data)
    except Exception as e:
        print('ERROR:', e)
        if 'pagging' in e or 'data' in e:
            break

count = 1 # for indexing
try:
    with open('new_cra_file.csv', mode='w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['No.','Id', 'Timestamp', 'Caption'])
        for i in data:
            print(i.keys())
            for j in i['data']:
                writer.writerow([count, j['id'], j['timestamp'], j['caption']])
                count += 1
except Exception as e:
    print('Error in writing...')
    print(e)