import csv
import json
import requests
import datetime
import time

API_KEY = ''
API_DOMAIN = ''

with open('mappedContents.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)

    for row in reversed(list(reader)):
      if row[0] == 'title':
        continue

      date =datetime.datetime.strptime(row[1], '%m/%d/%Y %H:%M:%S')
      obj = {
        'title': row[0],
        'category': row[2].replace('\"','').replace('[','').replace(']','').replace('\'','').replace(' ','').split(','),
        'importData': {
          'fieldId' : 'importData',
          'publishDate': date.isoformat() + ".00000+09:00",
          'content': row[3],
        }
      }
      jsonData = json.dumps(obj)
      headers = {'X-MICROCMS-API-KEY': API_KEY, 'Content-Type': 'application/json'}
      response = requests.post('https://' + API_DOMAIN +'/api/v1/content', data=jsonData, headers=headers)
      
      print('---------')
      print(row[0])
      print(response.text)
      time.sleep(5)

