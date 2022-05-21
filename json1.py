import json

data = '''
{
    "name" : "Yoav",
    "phone" : {
        "type" : "intl",
        "number" : "+1 202 640 3734"
    },
    "email" : {
        "hide" : "yes"
    }
}       
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:',  info["email"]["hide"])