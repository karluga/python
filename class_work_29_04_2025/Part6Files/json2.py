import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Janis"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Anna"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
