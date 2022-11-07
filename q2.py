# 2 Python object ko json data main convert karne ka program likho?
import json

a= {"name": "David", "class": "I", "age": 6}
g=json.dumps(a)
print(type(g))
print(g)