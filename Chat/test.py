import json

dict = {"type": "error", "data": "Invalid name message type"}
print(dict)
str = json.dumps(dict)
print(str)
dict2 = json.loads(str)
print(dict2)