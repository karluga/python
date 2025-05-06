import json

data = '''
{
  "name" : "Janis",
  "phone" : {
    "type" : "intl",
    "number" : "+371 1122"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
