import re
import csv
import os
import itertools

export_file_name = 'export.txt'
output_file_name = 'contents.csv'
output_category_file_name = 'category.csv'

f = open(export_file_name, 'r', encoding='UTF-8')

data = f.read()
splittedData = data.split('AUTHOR: ***')

def findItem(target, start, end):
  idx = target.find(start)
  finding = target[idx+len(start):]
  idx = finding.find(end)
  finded = finding[:idx]
  return finded

def findCategories(target): 
  elems = re.findall(r'CATEGORY: .*', target)
  formattedList= list(map(lambda item: item.removeprefix('CATEGORY: '), elems))
  return formattedList

def findContent(target):
  start= 'BODY:'
  idx = target.find(start)
  finding = target[idx+len(start):]
  replaced = finding.replace('-----\n--------', '').replace('-----\nEXTENDED BODY:', '')
  return replaced

def mapFunc(item):
  findContent(item)
  obj = {
    'title': findItem(item, 'TITLE: ', '\n'),
    'date': findItem(item, 'DATE: ', '\n'),
    'categories': findCategories(item),
    'content': findContent(item)
  }
      
  return obj

mapped = list(map(lambda item: mapFunc(item), splittedData))
del mapped[0]

f.close()

keys = mapped[0].keys()

def format2List(item):
  return [
    item.get('title'),
    item.get('date'),
    str(item.get('categories')).replace('[', '' ).replace(']', ''),
    item.get('content')
  ] 

if os.path.isfile(output_file_name):
  os.remove(output_file_name)

with open(output_file_name, 'w', encoding='UTF-8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for item in mapped: 
      writer.writerow(format2List(item))

categoriesList = list(set(list(itertools.chain.from_iterable(list(map(lambda item: item.get('categories'), mapped))))))

if os.path.isfile(output_category_file_name):
  os.remove(output_category_file_name)  
  
with open(output_category_file_name, 'w', encoding='UTF-8', newline="") as f:
  writer = csv.writer(f)
  writer.writerow(['id', 'name'])
  for index, item in enumerate(categoriesList): 
    writer.writerow(['', item])
