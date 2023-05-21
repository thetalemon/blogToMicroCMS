import csv
import os
import json

input_file = 'category.json'
mappedContents_file = 'mappedContents.csv'

with open(input_file, encoding='UTF-8') as f:
  jsonString = f.read()
  jsondata = json.loads(jsonString)

  categoryObj = {}
  
  for item in jsondata.get('contents'):
    categoryObj[item.get('name')] = item.get('id')

if os.path.isfile(mappedContents_file):
  os.remove(mappedContents_file)  

with open('contents.csv', encoding='UTF-8') as f:
  with open(mappedContents_file, 'w', encoding='UTF-8', newline="") as write:
    reader = csv.reader(f)
    writer = csv.writer(write)

    for index, row in enumerate(reader):
      if index == 0:
        writer.writerow(row)
        continue
      data = row[2].replace('\'', '').replace(' ', '').split(',')
      mapped = list(map(lambda item: categoryObj.get(item), data))

      row[2] = mapped
      writer.writerow(row)


