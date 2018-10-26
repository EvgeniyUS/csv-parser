import os, csv, json
from pprint import pprint
path = 'data/'
out = {}
out['commands'] = []
comDict = {}
for files in os.walk(path):
  for fileName in files[2]:
    with open(path+fileName, 'rb') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=';')
      for row in reader:
        if row['name'] not in comDict.keys():
          out['commands'].append(row)
        try:
          comDict[row['name']].append({'user':fileName.split('.')[0]})
        except KeyError, ke:
          comDict[row['name']] = [{'user':fileName.split('.')[0]}]
        row['param'] = comDict[row['name']]
with open('file.json', 'w') as fileJson:
  json.dump(out, fileJson, indent=4)
pprint(out)
