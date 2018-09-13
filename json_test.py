import json

configuration = '''
{
  "stations": [
    {
      "number": 1,
      "name": "Front",
      "active": false
    },
    {
      "number": 2,
      "name": "Back",
      "active": false
    }
  ],
  "cycles": [
    {
      "number": 1,
      "start time": "6:00",
      "days of week": [1,3,5],
      "stations": [1,2],
      "durations": [10,15],
      "enabled": true
    },
    {
      "number": 2,
      "start time": "7:00",
      "days of week": [2,4,6],
      "stations": [1,2],
      "durations": [5,8],
      "enabled": true
    }
  ]
}
'''

data = json.loads(configuration)
sorted_data = json.dumps(data, indent=2, sort_keys=True)

'''
with open('config.json', 'w') as outfile:
    json.dump(data, outfile, indent=2, sort_keys=True)
'''
with open('config.json') as f:
    loaded_data = json.load(f)
print(loaded_data['cycles'][0]['name'])
print(loaded_data['cycles'][1]['name'])
print(len(loaded_data['stations']))