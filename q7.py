# Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
d={}
for i in range (4):
    key=input("enter the key name")
    value=input("enter the value")
    d.update({key:value})
f=open("file.json","w")
k=json.dump(d,f,indent=4)
