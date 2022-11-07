# Q.3 Python object ko json string mai convert karne ka program likho?
import json
q={"ram":1,"mohan":2,"radha":3}
s=json.dumps(q)
print(type(s))
print(s)